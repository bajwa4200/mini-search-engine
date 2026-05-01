from searchengine.tokenizer import tokenize


def test_tokenize_lowercase():
    assert tokenize("Hello World!") == ["hello", "world"]
