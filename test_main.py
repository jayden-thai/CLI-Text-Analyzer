import pytest

from main import count_words, get_words, load_text


def test_word_normalization():
    text = "Hello! HELLO, world."

    result = get_words(text)

    assert result == ["hello", "hello", "world"]


def test_empty_text():
    text = ""

    result = get_words(text)

    assert result == []


def test_punctuation_text():
    text = ".,?! !!! !!! ?., ?., !?!? ,.,. ,,?"

    result = get_words(text)

    assert result == []


def test_repeated_text():
    text = "aba aba aba aba aba"

    result = get_words(text)

    assert result == ["aba", "aba", "aba", "aba", "aba"]


def test_word_counts():
    words = ["cat", "dog", "cat"]

    result = count_words(words)

    assert result["cat"] == 2
    assert result["dog"] == 1
    assert result["bird"] == 0


def test_load_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello Python!", encoding="utf-8")

    raw_text = load_text(str(file))

    assert raw_text == "Hello Python!"


def test_load_invalid_file(tmp_path):
    missing_file = tmp_path / "nonexistent_file.txt"

    with pytest.raises(FileNotFoundError):
        load_text(missing_file)