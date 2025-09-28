"""BM25 scoring."""

from __future__ import annotations

import math

from searchengine.index import InvertedIndex
from searchengine.tokenizer import tokenize


def bm25_score(
    index: InvertedIndex,
    query: str,
    doc_id: str,
    *,
    k1: float = 1.5,
    b: float = 0.75,
) -> float:
    doc = index.documents[doc_id]
    score = 0.0
    n_docs = len(index.documents)
    for term in tokenize(query):
        if term not in index.postings or doc_id not in index.postings[term]:
            continue
        df = len(index.postings[term])
        idf = math.log(1 + (n_docs - df + 0.5) / (df + 0.5))
        tf = index.postings[term][doc_id]
        denom = tf + k1 * (1 - b + b * doc.length / max(index.avg_doc_len, 1))
        score += idf * (tf * (k1 + 1)) / denom
    return score
