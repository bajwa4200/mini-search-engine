"""Search engine: index corpus and rank with BM25."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from searchengine.bm25 import bm25_score
from searchengine.index import InvertedIndex
from searchengine.tokenizer import tokenize


@dataclass
class SearchHit:
    doc_id: str
    score: float
    snippet: str


class SearchEngine:
    def __init__(self, index: InvertedIndex) -> None:
        self.index = index

    @classmethod
    def from_corpus(cls, corpus_dir: Path) -> SearchEngine:
        return cls(InvertedIndex.from_directory(corpus_dir))

    def search(self, query: str, limit: int = 10) -> list[SearchHit]:
        scores: list[SearchHit] = []
        for doc_id in self.index.documents:
            score = bm25_score(self.index, query, doc_id)
            if score > 0:
                scores.append(
                    SearchHit(
                        doc_id=doc_id,
                        score=score,
                        snippet=self._snippet(self.index.documents[doc_id].text, query),
                    )
                )
        scores.sort(key=lambda h: h.score, reverse=True)
        return scores[:limit]

    def _snippet(self, text: str, query: str, width: int = 80) -> str:
        terms = set(tokenize(query))
        words = text.split()
        for i, word in enumerate(words):
            if word.lower().strip(".,!?") in terms or any(t in word.lower() for t in terms):
                chunk = " ".join(words[i : i + 12])
                return chunk[:width]
        return text[:width]
