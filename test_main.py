from pathlib import Path

import pytest

from main import count_words, get_words, load_text


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello! HELLO, world.", ["hello", "hello", "world"]),
        ("", []),
        (".,?! !!! !!! ?., ?., !?!? ,.,. ,,?", []),
        ("aba aba aba aba aba", ["aba", "aba", "aba", "aba", "aba"]),
    ],
)
def test_get_words(text: str, expected: list[str]) -> None:
    assert get_words(text) == expected


@pytest.mark.parametrize(
    "words, expected, unexpected",
    [
        (["cat", "dog", "cat"], {"cat": 2, "dog": 1}, "bird"),
        (["chicken", "dog", "cat"], {"chicken": 1, "dog": 1, "cat": 1}, "frog"),
        (["chicken", "chicken", "cat", "chicken"], {"chicken": 3, "cat": 1}, "dog"),
    ],
)
def test_count_words(
    words: list[str], expected: dict[str, int], unexpected: str
) -> None:
    counts = count_words(words)
    assert counts == expected
    assert counts.get(unexpected) is None


@pytest.mark.parametrize(
    "filename, text",
    [
        ("test.txt", "Hello Python!"),
        ("file.txt", "Java is okay."),
        ("chicken.txt", "Secret message."),
    ],
)
def test_load_file(tmp_path: Path, filename: str, text: str) -> None:
    file = tmp_path / filename
    file.write_text(text, encoding="utf-8")

    raw_text = load_text(str(file))

    assert raw_text == text


def test_load_invalid_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "nonexistent_file.txt"

    with pytest.raises(FileNotFoundError):
        load_text(str(missing_file))
