"""Search CLI."""

from __future__ import annotations

import sys
from pathlib import Path

from searchengine.engine import SearchEngine

DEFAULT_CORPUS = Path(__file__).resolve().parent.parent / "data" / "corpus"


def main(argv: list[str] | None = None) -> None:
    argv = argv or sys.argv[1:]
    query = " ".join(argv) if argv else "python"
    engine = SearchEngine.from_corpus(DEFAULT_CORPUS)
    hits = engine.search(query)
    for hit in hits:
        print(f"{hit.score:.3f}  {hit.doc_id}: {hit.snippet}")


if __name__ == "__main__":
    main()
