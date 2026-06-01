Add a publication card to index.html.

Usage: /add-paper <arxiv_url> [venue] [year]

Steps:
1. Use WebFetch on the arXiv URL to extract: full paper title, full author list (in order), and submission year.
2. Derive the image filename: take the first 3 meaningful words of the title (skip: a, an, the, of, for, and, in, on, to, via, with, by), lowercase, join with underscores, append .png. Example: "Riemannian-Manifold Steering: ..." → riemannian_manifold_steering.png.
3. Check whether `assets/paper_figures/<filename>` exists. If not, stop and tell the user exactly which file to add.
4. Run from the repo root:
   ```
   python3 scripts/add_paper.py \
     --url "<arxiv_url>" \
     --title "<full title>" \
     --authors "<comma-separated author list>" \
     --year <year> \
     --venue "<venue or Preprint>" \
     --image <filename>
   ```
5. Show the script output. Ask if the user also wants a news item and whether to push.
