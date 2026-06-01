# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Amirali Abdullah's personal academic portfolio website, hosted via GitHub Pages at `amirali-abdullah.github.io`. Static site — no build system, bundler, or framework.

## Architecture

- **index.html** — Single-page site. Sections (delimited by `<!-- ===== SECTION ===== -->` banners): navbar, hero, about, news, publications, projects, comic, contact, footer
- **style.css** — All styles; layout uses flexbox with a 1000px max-width container pattern
- **assets/paper_figures/** — Thumbnail images for publication cards (PNG, named after the paper)
- **assets/comic/** — Comic strip images (WEBP, named `01_ai_detective.webp`, `02_...`, etc.)
- **.claude/commands/** — Project slash commands (see Skills below)

## Development

No build step. Open `index.html` directly in a browser or use any local server (e.g., `python3 -m http.server`).

## Deployment

Pushes to `main` are automatically deployed via GitHub Pages. No CI/CD beyond what GitHub Pages provides.

## Conventions

- Plain HTML/CSS only — no JavaScript, no frameworks, no preprocessors
- CSS classes follow a component-prefix pattern (e.g., `nav-inner`, `hero-text`, `pub-title`)
- The author's name appears as both "Amir Abdullah" and "Amirali Abdullah" — always use whichever form the paper itself uses, bolded with `<strong>`

## Publication card format

Each paper is a `.pub-card` div inside `<!-- ===== PUBLICATIONS ===== -->`. Cards are grouped under `<div class="pub-year">YEAR</div>` headers in reverse chronological order. New cards go immediately after the year header, above existing cards for that year.

```html
<div class="pub-card">
  <div class="pub-thumb"><img src="assets/paper_figures/FILENAME.png" alt="SHORT TITLE"></div>
  <div class="pub-body">
    <div class="pub-title">
      <a href="ARXIV_URL">FULL TITLE</a>
    </div>
    <div class="pub-venue-badge">VENUE OR "Preprint"</div>
    <div class="pub-authors">AUTHORS — bold the owner's name with &lt;strong&gt;</div>
    <div class="pub-meta">YEAR</div>
    <div class="pub-actions">
      <a href="ARXIV_URL" class="btn-action">ARXIV</a>
    </div>
  </div>
</div>
```

Thumbnail images live in `assets/paper_figures/`. Always verify the image exists before inserting a card — a missing image leaves a broken card on the live site.

## News item format

News items are `<li>` elements inside `<ul class="news-list">`. New items go at the top of the list.

```html
<li><span class="news-date">Mon YYYY</span> Text, optionally with <a href="...">links</a>.</li>
```

## Comic strip format

Comic strips live in `assets/comic/`, named sequentially (`01_...webp`, `02_...webp`). Each strip is a new release (not pages of a single strip). They appear in `<!-- ===== COMIC ===== -->` as `.comic-strip` divs — image links open full-size in a new tab. The navbar "Comic" link also opens the latest strip directly in a new tab.

## Skills

Two project slash commands are available:

- **`/add-paper <arXiv-URL> [venue] [year]`** — Fetches title/authors from arXiv, checks that a thumbnail image exists in `assets/paper_figures/`, then inserts a formatted pub card in the correct year section. Blocks if the image is missing.
- **`/add-news <date> <text>`** — Inserts a news item at the top of the news list.
