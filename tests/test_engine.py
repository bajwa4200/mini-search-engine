from pathlib import Path

from searchengine.engine import SearchEngine


def test_search_python():
    corpus = Path(__file__).resolve().parent.parent / "data" / "corpus"
    engine = SearchEngine.from_corpus(corpus)
    hits = engine.search("python machine learning")
    assert hits
    assert hits[0].doc_id == "python"
    assert hits[0].score > 0
