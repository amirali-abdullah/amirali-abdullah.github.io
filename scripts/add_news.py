#!/usr/bin/env python3
"""Usage: python3 scripts/add_news.py "Mon YYYY" "News text here" """
import sys
from pathlib import Path

MARKER = '<ul class="news-list">\n'


def main():
    if len(sys.argv) < 3:
        print('Usage: add_news.py "Mon YYYY" "text"')
        sys.exit(1)

    date = sys.argv[1]
    text = sys.argv[2]
    item = f'      <li><span class="news-date">{date}</span> {text}</li>\n'

    index = Path('index.html')
    html = index.read_text()

    if MARKER not in html:
        print("ERROR: could not find news list in index.html")
        sys.exit(1)

    idx = html.index(MARKER) + len(MARKER)
    index.write_text(html[:idx] + item + html[idx:])

    print(f"Added: [{date}] {text}")


if __name__ == '__main__':
    main()
