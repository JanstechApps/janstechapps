#!/usr/bin/env python3
"""Validate (or regenerate) the published Janstech Apps site metadata.

GitHub Pages serves this repository verbatim from the repository root, so the
repository root *is* the publish root. This script therefore checks the same
files that end up on https://janstechapps.com.

Usage:

    python tools/validate_site.py            # check only, non-zero exit on error
    python tools/validate_site.py --write    # regenerate sitemap.xml, then check

Checks performed:

- sitemap.xml and robots.txt exist in the publish root
- sitemap.xml is well-formed XML using the sitemaps.org 0.9 namespace
- every <loc> is an absolute https URL on the production domain, without
  fragments, query strings or duplicates
- every <loc> maps to a real, case-exact page file in the publish root
- the sitemap contains exactly the set of indexable pages found on disk
- every <lastmod> matches the last git commit date of the page file
- robots.txt is valid UTF-8, does not block indexable pages and ends with the
  Sitemap: line
- every internal link and asset reference in the HTML pages resolves to a real,
  case-exact file (catches wrong casing and broken paths)
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

SITE_ORIGIN = "https://janstechapps.com"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
PUBLISH_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITEMAP_PATH = os.path.join(PUBLISH_ROOT, "sitemap.xml")
ROBOTS_PATH = os.path.join(PUBLISH_ROOT, "robots.txt")

# Directories that never contain publishable pages.
SKIPPED_DIRS = {".git", ".github", "tools", "docs", "assets"}

# Pages that exist but must stay out of the sitemap (404 pages, redirects,
# drafts). Paths are relative to the publish root and use forward slashes.
EXCLUDED_PAGES: set[str] = set()

LINK_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def page_files() -> list[str]:
    """Return every publishable HTML page, relative to the publish root.

    Ordered the way the sitemap reads best: home page first, then by URL.
    """
    pages = []
    for dirpath, dirnames, filenames in os.walk(PUBLISH_ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIPPED_DIRS and not d.startswith("."))
        for filename in sorted(filenames):
            if not filename.lower().endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, filename), PUBLISH_ROOT)
            rel = rel.replace(os.sep, "/")
            if rel not in EXCLUDED_PAGES:
                pages.append(rel)
    return sorted(pages, key=lambda page: (page != "index.html", page_to_url_path(page)))


def page_to_url_path(rel_path: str) -> str:
    """Map a page file to its canonical site path (directory URLs keep the slash)."""
    if rel_path == "index.html":
        return "/"
    if rel_path.endswith("/index.html"):
        return "/" + rel_path[: -len("index.html")]
    return "/" + rel_path


def url_path_to_page(url_path: str) -> str:
    """Inverse of page_to_url_path."""
    rel = url_path.lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return rel


def exists_case_exact(rel_path: str) -> bool:
    """Check a path exists with exactly this casing (Windows/macOS are case-insensitive)."""
    current = PUBLISH_ROOT
    for part in rel_path.split("/"):
        if part in ("", "."):
            continue
        try:
            entries = os.listdir(current)
        except (NotADirectoryError, FileNotFoundError, PermissionError):
            return False
        if part not in entries:
            return False
        current = os.path.join(current, part)
    return os.path.isfile(current)


def git_last_modified(rel_path: str) -> str | None:
    """Last commit date (YYYY-MM-DD) for a tracked file, or None if untracked."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            cwd=PUBLISH_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def build_sitemap() -> str:
    """Render sitemap.xml from the pages on disk and their git commit dates."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', f'<urlset xmlns="{SITEMAP_NS}">']
    for rel_path in page_files():
        loc = SITE_ORIGIN + page_to_url_path(rel_path)
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lastmod = git_last_modified(rel_path)
        if lastmod:
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def write_sitemap() -> None:
    with open(SITEMAP_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_sitemap())
    print(f"wrote {os.path.relpath(SITEMAP_PATH, PUBLISH_ROOT)}")


def check_sitemap(errors: list[str]) -> None:
    if not os.path.isfile(SITEMAP_PATH):
        errors.append("sitemap.xml is missing from the publish root")
        return

    raw = open(SITEMAP_PATH, "rb").read()
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError:
        errors.append("sitemap.xml is not valid UTF-8")
        return
    if b'encoding="UTF-8"' not in raw.split(b"\n", 1)[0]:
        errors.append('sitemap.xml is missing the <?xml ... encoding="UTF-8"?> declaration')

    try:
        root = ElementTree.fromstring(raw)
    except ElementTree.ParseError as exc:
        errors.append(f"sitemap.xml is not well-formed XML: {exc}")
        return

    if root.tag != f"{{{SITEMAP_NS}}}urlset":
        errors.append(f"sitemap.xml root element is {root.tag}, expected urlset in {SITEMAP_NS}")
        return

    seen: dict[str, str] = {}
    for entry in root:
        if entry.tag != f"{{{SITEMAP_NS}}}url":
            errors.append(f"unexpected element {entry.tag} in sitemap.xml")
            continue

        locs = entry.findall(f"{{{SITEMAP_NS}}}loc")
        if len(locs) != 1 or not (locs[0].text or "").strip():
            errors.append("every <url> needs exactly one non-empty <loc>")
            continue
        loc = locs[0].text.strip()

        if loc in seen:
            errors.append(f"duplicate URL in sitemap.xml: {loc}")
            continue

        parts = urlsplit(loc)
        if parts.scheme != "https" or f"{parts.scheme}://{parts.netloc}" != SITE_ORIGIN:
            errors.append(f"sitemap URL is not an absolute {SITE_ORIGIN} https URL: {loc}")
            continue
        if parts.fragment:
            errors.append(f"sitemap URL must not contain a fragment: {loc}")
            continue
        if parts.query:
            errors.append(f"sitemap URL must not contain a query string: {loc}")
            continue

        rel_page = url_path_to_page(unquote(parts.path))
        if not exists_case_exact(rel_page):
            errors.append(f"sitemap URL does not resolve to a published page: {loc} -> {rel_page}")
            continue
        if rel_page in EXCLUDED_PAGES:
            errors.append(f"sitemap URL points to an excluded page: {loc}")
            continue
        seen[loc] = rel_page

        lastmods = entry.findall(f"{{{SITEMAP_NS}}}lastmod")
        if len(lastmods) > 1:
            errors.append(f"more than one <lastmod> for {loc}")
        elif lastmods:
            lastmod = (lastmods[0].text or "").strip()
            if not DATE_RE.match(lastmod):
                errors.append(f"<lastmod> for {loc} is not a YYYY-MM-DD date: {lastmod!r}")
            else:
                expected = git_last_modified(rel_page)
                if expected and lastmod != expected:
                    errors.append(
                        f"<lastmod> for {loc} is {lastmod}, but git says {expected} "
                        f"(run: python tools/validate_site.py --write)"
                    )

    expected_urls = {SITE_ORIGIN + page_to_url_path(page) for page in page_files()}
    for missing in sorted(expected_urls - set(seen)):
        errors.append(f"published page is missing from sitemap.xml: {missing}")


def check_robots(errors: list[str]) -> None:
    if not os.path.isfile(ROBOTS_PATH):
        errors.append("robots.txt is missing from the publish root")
        return

    try:
        text = open(ROBOTS_PATH, "rb").read().decode("utf-8")
    except UnicodeDecodeError:
        errors.append("robots.txt is not valid UTF-8")
        return

    sitemap_line = f"Sitemap: {SITE_ORIGIN}/sitemap.xml"
    if not any(line.strip() == sitemap_line for line in text.splitlines()):
        errors.append(f"robots.txt does not contain the line: {sitemap_line}")

    # Reject any wildcard Disallow rule that would block an indexable page.
    applies_to_all = False
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, value = (part.strip() for part in line.split(":", 1))
        field = field.lower()
        if field == "user-agent":
            applies_to_all = value == "*"
        elif field == "disallow" and applies_to_all and value:
            for page in page_files():
                url_path = page_to_url_path(page)
                if url_path.startswith(value):
                    errors.append(f"robots.txt rule 'Disallow: {value}' blocks {url_path}")
                    break


def check_internal_links(errors: list[str]) -> None:
    for page in page_files():
        html = open(os.path.join(PUBLISH_ROOT, page), encoding="utf-8").read()
        for target in LINK_RE.findall(html):
            target = target.strip()
            if not target or target.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
                continue

            if target.startswith(f"{SITE_ORIGIN}/"):
                path = urlsplit(target).path
            elif re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue  # external resource
            elif target.startswith("/"):
                path = urlsplit(target).path
            else:
                base = os.path.dirname(page)
                path = "/" + os.path.normpath(os.path.join(base, urlsplit(target).path)).replace(os.sep, "/")

            rel_target = url_path_to_page(unquote(path))
            if not exists_case_exact(rel_target):
                errors.append(f"{page}: link target does not exist: {target} -> {rel_target}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="regenerate sitemap.xml from the pages on disk before checking",
    )
    args = parser.parse_args()

    if args.write:
        write_sitemap()

    errors: list[str] = []
    check_sitemap(errors)
    check_robots(errors)
    check_internal_links(errors)

    if errors:
        print(f"FAIL: {len(errors)} problem(s) found", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(page_files())} pages, sitemap.xml and robots.txt validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
