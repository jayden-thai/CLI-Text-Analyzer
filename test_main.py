from main import count_words, get_words


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