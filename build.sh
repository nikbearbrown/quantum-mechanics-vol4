#!/bin/bash
set -e

BOOK_SLUG="quantum-mechanics-vol4"
METADATA="metadata.yaml"
OUTPUT_DIR="output"

mkdir -p "$OUTPUT_DIR"

build_edition () {
  local SRC_DIR="$1"   # chapters | generic
  local SUFFIX="$2"    # "" | -openstax
  local COMBINED="$OUTPUT_DIR/combined$SUFFIX.md"

  # concatenate; metadata goes in via --metadata-file so stray '---' blocks
  # in chapter prose are never parsed (and dropped) as YAML
  cat "$SRC_DIR"/*.md > "$COMBINED"

  # chapter files reference images as ../images/ (relative to the source dir);
  # pandoc runs from the book root, so rewrite to images/
  sed -i 's|](\.\./images/|](images/|g' "$COMBINED"

  # EPUB input: make \tag{N.M} equation numbers visible (MathML drops \tag);
  # the HTML build keeps the original so MathJax renders native right-aligned tags
  local COMBINED_EPUB="$OUTPUT_DIR/combined$SUFFIX-epub.md"
  sed 's/\\tag{\([^}]*\)}/\\qquad \\text{(\1)}/g' "$COMBINED" > "$COMBINED_EPUB"

  pandoc "$COMBINED_EPUB" \
    --from markdown-yaml_metadata_block \
    --metadata-file="$METADATA" \
    --to epub3 \
    --mathml \
    --epub-cover-image=cover.jpg \
    --css=styles/kindle.css \
    --css=styles/kindle-book.css \
    --toc --toc-depth=2 \
    --output="$OUTPUT_DIR/$BOOK_SLUG$SUFFIX.epub"

  pandoc "$COMBINED" \
    --from markdown-yaml_metadata_block \
    --metadata-file="$METADATA" \
    --to html5 \
    --standalone \
    --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js \
    --css=styles/kindle.css \
    --css=styles/kindle-book.css \
    --toc \
    --output="$OUTPUT_DIR/$BOOK_SLUG$SUFFIX.html"

  echo "Built: $OUTPUT_DIR/$BOOK_SLUG$SUFFIX.epub"
  echo "Built: $OUTPUT_DIR/$BOOK_SLUG$SUFFIX.html"
}

build_edition chapters ""
[ -d generic ] && build_edition generic "-openstax"
