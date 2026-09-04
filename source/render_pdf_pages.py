"""Rasterize each final PDF page with bundled PDFium for visual QA."""

from __future__ import annotations

import argparse
from pathlib import Path

import pypdfium2 as pdfium


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("outdir", type=Path)
    parser.add_argument("--dpi", type=int, default=200)
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)
    document = pdfium.PdfDocument(str(args.pdf))
    scale = args.dpi / 72.0
    for index in range(len(document)):
        page = document[index]
        image = page.render(scale=scale).to_pil().convert("RGB")
        target = args.outdir / f"page-{index + 1}.png"
        image.save(target, optimize=True)
        print(target)


if __name__ == "__main__":
    main()
