# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is Amirali Abdullah's personal academic portfolio website, hosted via GitHub Pages at `amirali-abdullah.github.io`. It is a static site with no build system, bundler, or framework.

## Architecture

- **index.html** — Single-page site with sections: navbar, hero, about, news, publications, projects, contact, footer
- **style.css** — All styles; layout uses flexbox with a 1000px max-width container pattern
- **assets/** — Static images (profile photo)

## Development

No build step. Open `index.html` directly in a browser or use any local server (e.g., `python3 -m http.server`).

## Deployment

Pushes to `main` are automatically deployed via GitHub Pages. There is no CI/CD pipeline or build process beyond what GitHub Pages provides.

## Conventions

- Plain HTML/CSS only — no JavaScript, no frameworks, no preprocessors
- Sections in `index.html` are delimited with HTML comment banners (`<!-- ===== SECTION ===== -->`)
- CSS classes follow a component-prefix pattern (e.g., `nav-inner`, `hero-text`, `pub-title`)
