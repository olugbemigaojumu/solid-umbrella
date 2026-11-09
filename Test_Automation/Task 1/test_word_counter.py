import pytest
from word_counter import count_word_matches


# ---------- Exercise 1: Basic parameterized tests ----------
@pytest.mark.parametrize(
    "text, target, expected",
    [
        pytest.param("The cat sat on the mat", "cat", 1, id="single-match"),
        pytest.param("Dog dog DOG dOg", "dog", 4, id="case-insensitive"),
        pytest.param("Hello world", "world", 1, id="match-last-word"),
        pytest.param("hello hello HELLO", "hello", 3, id="repeated-mixed-case"),
        pytest.param("No matches here", "yes", 0, id="no-match"),
        pytest.param("catcat cat catdog", "cat", 1, id="substring-not-counted"),
        pytest.param("a a a", "a", 3, id="single-letter-repeated"),
    ],
)
def test_basic_matches(text, target, expected):
    assert count_word_matches(text, target) == expected


# ---------- Exercise 2: Edge cases ----------
@pytest.mark.parametrize(
    "text, target, expected",
    [
        pytest.param("", "word", 0, id="empty-text"),
        pytest.param("hello world", "", 0, id="empty-target"),
        pytest.param("", "", 0, id="both-empty"),
        pytest.param("hello     world", "world", 1, id="multiple-spaces"),
        pytest.param(" cat ", "cat", 1, id="leading-trailing-spaces"),
        pytest.param("cat,dog cat", "cat", 1, id="punctuation-not-handled"),
        pytest.param("x y z", "x", 1, id="single-character"),
    ],
)
def test_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected


# ---------- Exercise 3: Negative tests ----------
@pytest.mark.parametrize(
    "text, target",
    [
        pytest.param(None, "word", id="none-text"),
        pytest.param("hello world", None, id="none-target"),
        pytest.param(123, "word", id="int-text"),
        pytest.param("hello world", 456, id="int-target"),
        pytest.param(["hello", "world"], "world", id="list-text"),
        pytest.param("hello world", ["world"], id="list-target"),
    ],
)
def test_invalid_inputs_raise_type_error(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)