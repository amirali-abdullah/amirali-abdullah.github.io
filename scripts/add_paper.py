#!/usr/bin/env python3
"""
Insert a publication card into index.html.

Usage:
  python3 scripts/add_paper.py \\
    --url <arxiv_url> \\
    --title "Full Paper Title" \\
    --authors "Author One, Author Two, Amir Abdullah" \\
    --year 2026 \\
    [--venue "ICML 2026"] \\
    [--image riemannian_steering.png]

If --image is omitted, the slug is derived from the first 3 meaningful title words.
Exits with code 1 and a clear message if the image file is missing.
"""
import sys
import re
import argparse
from pathlib import Path

OWNER_VARIANTS = {'amir abdullah', 'amirali abdullah'}


def image_slug(title):
    stop = {'a', 'an', 'the', 'of', 'for', 'and', 'in', 'on', 'to', 'via', 'with', 'by'}
    words = re.sub(r'[^a-z0-9 ]', '', title.lower()).split()
    words = [w for w in words if w not in stop]
    return '_'.join(words[:3]) + '.png'


def format_authors(authors_str):
    parts = []
    for name in [a.strip() for a in authors_str.split(',')]:
        if name.lower() in OWNER_VARIANTS:
            parts.append(f'<strong>{name}</strong>')
        else:
            parts.append(name)
    return ', '.join(parts)


def make_card(title, authors_html, url, venue, year, img_file):
    return (
        f'\n  <div class="pub-card">\n'
        f'    <div class="pub-thumb"><img src="assets/paper_figures/{img_file}" alt="{title}"></div>\n'
        f'    <div class="pub-body">\n'
        f'      <div class="pub-title">\n'
        f'        <a href="{url}">{title}</a>\n'
        f'      </div>\n'
        f'      <div class="pub-venue-badge">{venue}</div>\n'
        f'      <div class="pub-authors">{authors_html}</div>\n'
        f'      <div class="pub-meta">{year}</div>\n'
        f'      <div class="pub-actions">\n'
        f'        <a href="{url}" class="btn-action">ARXIV</a>\n'
        f'      </div>\n'
        f'    </div>\n'
        f'  </div>\n'
    )


def insert_card(html, card, year):
    year_marker = f'<div class="pub-year">{year}</div>'
    if year_marker in html:
        idx = html.index(year_marker) + len(year_marker)
        return html[:idx] + card + html[idx:]

    existing_years = [int(y) for y in re.findall(r'<div class="pub-year">(\d+)</div>', html)]
    for ey in sorted(existing_years, reverse=True):
        if int(year) > ey:
            marker = f'<div class="pub-year">{ey}</div>'
            idx = html.index(marker)
            new_block = f'\n  <!-- {year} -->\n  {year_marker}\n{card}\n  '
            return html[:idx] + new_block + html[idx:]

    print("ERROR: could not find an insertion point in index.html")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--title', required=True)
    parser.add_argument('--authors', required=True)
    parser.add_argument('--year', required=True)
    parser.add_argument('--venue', default='Preprint')
    parser.add_argument('--image', default=None)
    args = parser.parse_args()

    img_file = args.image or image_slug(args.title)
    img_path = Path('assets/paper_figures') / img_file
    if not img_path.exists():
        print(f"ERROR: Missing thumbnail. Please add: {img_path}")
        print(f"(Derived from title: \"{args.title}\")")
        sys.exit(1)

    authors_html = format_authors(args.authors)
    card = make_card(args.title, authors_html, args.url, args.venue, args.year, img_file)

    index = Path('index.html')
    index.write_text(insert_card(index.read_text(), card, args.year))

    print(f"Done.")
    print(f"  Title:  {args.title}")
    print(f"  Image:  assets/paper_figures/{img_file}")
    print(f"  Venue:  {args.venue}, Year: {args.year}")


if __name__ == '__main__':
    main()
