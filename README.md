# Mini Search Engine

A readable search engine skeleton: tokenize documents, build an inverted index, score queries with BM25, and return ranked snippets. Ships with a tiny text corpus under `data/corpus/`.

## Quick start

```bash
pip install -e ".[dev]"
mini-search python machine learning
```

## Tests

```bash
python -m pytest -q
```

## Layout

```
mini-search-engine/
├── data/corpus/
├── searchengine/
│   ├── tokenizer.py
│   ├── index.py
│   ├── bm25.py
│   ├── engine.py
│   └── cli.py
└── tests/
```

## License

MIT — see [LICENSE](LICENSE).
