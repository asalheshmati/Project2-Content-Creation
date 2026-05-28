"""Utilities for extracting source text from articles and PDFs."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader


def _clean_text(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", (text or "").strip())
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def _unique_lines(text: str) -> str:
    seen = set()
    lines = []
    for raw_line in (text or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line in seen:
            continue
        seen.add(line)
        lines.append(line)
    return "\n".join(lines)


def _truncate(text: str, max_chars: int = 9000) -> str:
    cleaned = _clean_text(text)
    if len(cleaned) <= max_chars:
        return cleaned
    return cleaned[:max_chars].rsplit(" ", 1)[0].strip()


def extract_article_text(article_url: str) -> str:
    """Fetch an article URL and extract visible text."""
    if not article_url:
        return ""

    response = requests.get(
        article_url,
        timeout=20,
        headers={"User-Agent": "Mozilla/5.0 (compatible; RecruAI/1.0)"},
    )
    response.raise_for_status()
    return extract_html_text(response.text)


def extract_html_text(html: str) -> str:
    """Extract article-like text from HTML."""
    soup = BeautifulSoup(html or "", "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    pieces = []

    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    if title:
        pieces.append(title)

    containers = []
    for selector in ("article", "main"):
        containers.extend(soup.find_all(selector))

    if not containers:
        containers = [soup]

    for container in containers:
        for tag in container.find_all(["h1", "h2", "h3", "p", "li"]):
            text = tag.get_text(" ", strip=True)
            if text:
                pieces.append(text)

    return _truncate(_unique_lines("\n".join(pieces)))


def extract_pdf_text(pdf_path) -> str:
    """Extract text from a PDF file path."""
    pdf_path = _normalize_file_path(pdf_path)
    if not pdf_path:
        return ""

    source = Path(pdf_path)
    if not source.exists():
        raise RuntimeError(f"PDF file not found: {pdf_path}")

    reader = PdfReader(str(source))
    pieces = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        if page_text.strip():
            pieces.append(page_text)

    return _truncate(_unique_lines("\n".join(pieces)))


def _normalize_file_path(file_value: Any) -> str:
    """Convert Gradio upload values or plain paths into a usable file path string."""
    if not file_value:
        return ""

    if isinstance(file_value, (str, Path)):
        return str(file_value)

    if isinstance(file_value, dict):
        for key in ("path", "name", "filepath"):
            value = file_value.get(key)
            if value:
                return str(value)

    for attr in ("path", "name"):
        value = getattr(file_value, attr, None)
        if value:
            return str(value)

    return str(file_value)


def build_source_text(article_url: str = "", uploaded_pdf=None) -> str:
    """Combine article and PDF source text into one prompt-ready block."""
    article_text = extract_article_text(article_url) if article_url else ""
    pdf_text = ""
    if uploaded_pdf:
        try:
            pdf_text = extract_pdf_text(uploaded_pdf)
        except Exception as exc:
            raise RuntimeError(f"Could not read the uploaded PDF: {exc}") from exc

    if article_text and pdf_text:
        combined = (
            "Article source:\n"
            f"{article_text}\n\n"
            "PDF source:\n"
            f"{pdf_text}"
        )
    elif article_text:
        combined = f"Article source:\n{article_text}"
    elif pdf_text:
        combined = f"PDF source:\n{pdf_text}"
    else:
        combined = ""

    return _truncate(combined, max_chars=12000)
