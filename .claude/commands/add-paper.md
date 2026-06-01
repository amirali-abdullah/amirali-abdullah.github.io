Add a publication card to the publications section of index.html.

Usage: /add-paper <arXiv-URL> [venue] [year]

Steps:
1. Fetch the arXiv page to extract the paper title and full author list.
2. Determine the year: use the provided year argument, or infer from the arXiv submission date.
3. Derive an image filename: lowercase the first significant word(s) of the title, replace spaces with underscores, e.g. "riemannian_steering.png". Check whether `assets/paper_figures/<filename>.png` exists. If it does not exist, stop and tell the user: "Please add a thumbnail image at assets/paper_figures/<filename>.png before I insert the card." Do not insert a broken card.
4. Format the author list. Bold whichever form of the author's name appears in the paper ("Amir Abdullah" or "Amirali Abdullah") using `<strong>`.
5. Find the correct year block in index.html (look for `<div class="pub-year">YEAR</div>`). If no block exists for that year, create one in the right chronological position. Insert the new pub card immediately after the year header, above any existing cards for that year.
6. Use this exact card format:

```html
  <div class="pub-card">
    <div class="pub-thumb"><img src="assets/paper_figures/FILENAME" alt="TITLE"></div>
    <div class="pub-body">
      <div class="pub-title">
        <a href="ARXIV_URL">FULL TITLE</a>
      </div>
      <div class="pub-venue-badge">VENUE</div>
      <div class="pub-authors">AUTHOR LIST</div>
      <div class="pub-meta">YEAR</div>
      <div class="pub-actions">
        <a href="ARXIV_URL" class="btn-action">ARXIV</a>
      </div>
    </div>
  </div>
```

7. If no venue was provided, use "Preprint".
8. After inserting, ask the user if they also want a news item added for this paper.
