#!/usr/bin/env python3
"""Convert a Markdown report to a simple PDF.

Usage:
  python markdown_to_pdf.py input.md [output.pdf]

This intentionally keeps formatting simple and robust for research reports:
headings, bullets, paragraphs, and tables are rendered as readable text.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def clean_inline(markdown: str) -> str:
    text = markdown.strip()
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='STSong-Light'>\1</font>", text)
    return text.replace("&", "&amp;").replace("<b>", "<b>").replace("</b>", "</b>")


def line_to_paragraph(line: str, styles: dict[str, ParagraphStyle]) -> tuple[Paragraph, int]:
    stripped = line.rstrip()
    if not stripped:
        return Paragraph("", styles["Body"]), 4

    if stripped.startswith("# "):
        return Paragraph(clean_inline(stripped[2:]), styles["Title"]), 8
    if stripped.startswith("## "):
        return Paragraph(clean_inline(stripped[3:]), styles["Heading2"]), 6
    if stripped.startswith("### "):
        return Paragraph(clean_inline(stripped[4:]), styles["Heading3"]), 5
    if stripped.startswith("- "):
        return Paragraph("• " + clean_inline(stripped[2:]), styles["Body"]), 3
    if stripped.startswith("|"):
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(set(cell) <= {"-", ":"} for cell in cells if cell):
            return Paragraph("", styles["Body"]), 0
        return Paragraph(clean_inline(" | ".join(cells)), styles["TableLine"]), 3
    return Paragraph(clean_inline(stripped), styles["Body"]), 4


def convert(markdown_path: Path, pdf_path: Path) -> None:
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="STSong-Light",
            fontSize=18,
            leading=24,
            spaceAfter=8,
        ),
        "Heading2": ParagraphStyle(
            "Heading2",
            parent=base["Heading2"],
            fontName="STSong-Light",
            fontSize=14,
            leading=19,
            spaceBefore=8,
            spaceAfter=5,
        ),
        "Heading3": ParagraphStyle(
            "Heading3",
            parent=base["Heading3"],
            fontName="STSong-Light",
            fontSize=12,
            leading=17,
            spaceBefore=6,
            spaceAfter=4,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=9,
            leading=13,
        ),
        "TableLine": ParagraphStyle(
            "TableLine",
            parent=base["BodyText"],
            fontName="STSong-Light",
            fontSize=7,
            leading=10,
        ),
    }

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=14 * mm,
        leftMargin=14 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
    )
    story = []
    for line in markdown_path.read_text(encoding="utf-8").splitlines():
        paragraph, gap = line_to_paragraph(line, styles)
        if paragraph.getPlainText():
            story.append(paragraph)
        if gap:
            story.append(Spacer(1, gap))
    doc.build(story)


def main(argv: list[str]) -> int:
    if not argv or len(argv) > 2:
        print("Usage: markdown_to_pdf.py input.md [output.pdf]", file=sys.stderr)
        return 2
    markdown_path = Path(argv[0]).expanduser().resolve()
    if not markdown_path.is_file():
        print(f"Input Markdown not found: {markdown_path}", file=sys.stderr)
        return 1
    pdf_path = Path(argv[1]).expanduser().resolve() if len(argv) == 2 else markdown_path.with_suffix(".pdf")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    convert(markdown_path, pdf_path)
    print(pdf_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
