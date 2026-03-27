"""Simple tokenizer for indexing and search."""

from __future__ import annotations

import re

_TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric tokens."""
    return _TOKEN_RE.findall(text.lower())
