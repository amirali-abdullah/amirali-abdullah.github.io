Add a news item to the top of the news list in index.html.

Usage: /add-news <date> <text>

- Date format: "Mon YYYY" (e.g. "Jun 2026") or just "YYYY" for year-only items.
- Insert as the first `<li>` inside `<ul class="news-list">`.
- Use this exact format:

```html
      <li><span class="news-date">DATE</span> TEXT</li>
```

- If the text references a paper or section on the page, link it with an `<a href="...">` tag.
- After inserting, confirm what was added and ask if the user wants to push.
