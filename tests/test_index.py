from pathlib import Path

from searchengine.index import InvertedIndex


def test_build_index_from_corpus():
    corpus = Path(__file__).resolve().parent.parent / "data" / "corpus"
    idx = InvertedIndex.from_directory(corpus)
    assert "python" in idx.postings
    assert len(idx.documents) >= 3
