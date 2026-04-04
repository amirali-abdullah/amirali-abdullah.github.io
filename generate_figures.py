#!/usr/bin/env python3
"""
Generate paper thumbnail images using OpenAI's DALL-E API.
Requires: pip install openai
Set OPENAI_API_KEY environment variable before running.

Usage:
    export OPENAI_API_KEY="sk-..."
    python3 generate_figures.py
"""

import os
import ssl
import urllib.request
from openai import OpenAI

# Handle macOS SSL certificate issue
ssl_ctx = ssl.create_default_context()
try:
    import certifi
    ssl_ctx.load_verify_locations(certifi.where())
except ImportError:
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_NONE

client = OpenAI()

OUTPUT_DIR = "assets/paper_figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Papers that need generated figures (those currently using SVG placeholders)
papers = {
    "robust_steering": (
        "Abstract scientific illustration for a paper about understanding and mitigating "
        "dataset corruption in language model steering. Show corrupted/noisy data points "
        "being filtered and cleaned. Minimal, geometric style with blue and gray tones. "
        "Square format, clean white background, no text."
    ),
    "beyond_linear": (
        "Abstract scientific illustration for a paper about multi-attribute steering "
        "control in language models, going beyond linear methods. Show multiple colorful "
        "directional vectors in a high-dimensional space converging on a target. "
        "Minimal geometric style, blue and purple tones. Square format, clean background, no text."
    ),
    "activation_transfer": (
        "Abstract scientific illustration for a paper about transferring activation space "
        "interventions between different large language models. Show two neural network "
        "architectures with glowing activation patterns being mapped from one to the other. "
        "Minimal geometric style, blue and teal tones. Square format, clean background, no text."
    ),
    "sycophancy": (
        "Abstract scientific illustration for a paper about decomposing sycophancy in AI "
        "into atomic psychometric personality traits. Show overlapping translucent circles "
        "or trait components combining together. Minimal geometric style, warm purple and "
        "blue tones. Square format, clean background, no text."
    ),
    "distribution_sae": (
        "Abstract scientific illustration for a paper about distribution-aware feature "
        "selection in sparse autoencoders. Show a probability distribution with highlighted "
        "selected features and a sparse encoding layer. Minimal geometric style, blue and "
        "green tones. Square format, clean background, no text."
    ),
    "beyond_monoliths": (
        "Abstract scientific illustration for a paper about expert orchestration in large "
        "language models, moving beyond monolithic architectures. Show a grid of specialized "
        "expert modules being coordinated by a central orchestrator. Minimal geometric style, "
        "blue and orange tones. Square format, clean background, no text."
    ),
    "feedback_patterns": (
        "Abstract scientific illustration for a paper about interpreting learned feedback "
        "patterns in large language models using sparse autoencoders. Show circular feedback "
        "loops with decoded feature patterns. Minimal geometric style, blue and purple tones. "
        "Square format, clean background, no text."
    ),
    "isoperimetric": (
        "Abstract mathematical illustration for a paper about directed isoperimetric "
        "inequalities and Bregman divergence nearest neighbor lower bounds. Show a geometric "
        "polygon with directed boundary edges and interior volume highlighted. Minimal "
        "geometric style, blue and gray tones. Square format, clean background, no text."
    ),
    "spectral_nn": (
        "Abstract mathematical illustration for a paper about spectral approaches to "
        "nearest neighbor search. Show concentric spectral rings with data points and a "
        "highlighted nearest neighbor cluster. Minimal geometric style, blue and teal tones. "
        "Square format, clean background, no text."
    ),
}

def generate_image(name, prompt):
    output_path = os.path.join(OUTPUT_DIR, f"{name}.png")

    # Skip if a PNG already exists (don't overwrite user-provided figures)
    if os.path.exists(output_path):
        print(f"  Skipping {name} — PNG already exists")
        return

    print(f"  Generating {name}...")
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    with urllib.request.urlopen(image_url, context=ssl_ctx) as resp:
        with open(output_path, 'wb') as f:
            f.write(resp.read())
    print(f"  Saved {output_path}")


def main():
    print("Generating paper thumbnails with DALL-E 3...\n")

    for name, prompt in papers.items():
        try:
            generate_image(name, prompt)
        except Exception as e:
            print(f"  ERROR generating {name}: {e}")

    print("\nDone! Generated images are in assets/paper_figures/")
    print("After generating, update index.html to use .png instead of .svg for these papers.")
    print("\nTo swap SVGs for PNGs in index.html, run:")
    print("  sed -i '' 's/\\.svg\"/.png\"/g' index.html")


if __name__ == "__main__":
    main()
