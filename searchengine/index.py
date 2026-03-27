"""Inverted index over tokenized documents."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from searchengine.tokenizer import tokenize


@dataclass
class Document:
    doc_id: str
    text: str
    length: int


@dataclass
class InvertedIndex:
    documents: dict[str, Document] = field(default_factory=dict)
    postings: dict[str, dict[str, int]] = field(default_factory=dict)
    avg_doc_len: float = 0.0

    @classmethod
    def from_directory(cls, corpus_dir: Path) -> InvertedIndex:
        idx = cls()
        for path in sorted(corpus_dir.glob("*.txt")):
            text = path.read_text(encoding="utf-8")
            doc_id = path.stem
            idx.add_document(doc_id, text)
        return idx

    def add_document(self, doc_id: str, text: str) -> None:
        tokens = tokenize(text)
        self.documents[doc_id] = Document(doc_id=doc_id, text=text, length=len(tokens))
        counts = Counter(tokens)
        for term, tf in counts.items():
            self.postings.setdefault(term, {})[doc_id] = tf
        lengths = [d.length for d in self.documents.values()]
        self.avg_doc_len = sum(lengths) / len(lengths) if lengths else 0.0
