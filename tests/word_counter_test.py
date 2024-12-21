import pytest
from wc.word_counter import wc


# Helper function to create a temporary file for testing
@pytest.fixture
def create_temp_file(tmp_path):
    def _create_file(name, content):
        file_path = tmp_path / name
        file_path.write_text(content)
        return str(file_path)

    return _create_file


# Test cases
def test_lines_only(create_temp_file):
    file_path = create_temp_file("test1.txt", "Hello world\nThis is a test\nAnother line")
    result = wc(file_path, l_option=True)
    assert result == "Lines number: 3"


def test_words_only(create_temp_file):
    file_path = create_temp_file("test2.txt", "Hello world\nThis is a test")
    result = wc(file_path, w_option=True)
    assert result == "Words number: 6"


def test_chars_only(create_temp_file):
    file_path = create_temp_file("test3.txt", "Hello world\nThis is a test")
    result = wc(file_path, c_option=True)
    assert result == "Chars number: 21"


def test_all_options(create_temp_file):
    file_path = create_temp_file("test4.txt", "Hello world\nThis is a test\n")
    result = wc(file_path, l_option=True, w_option=True, c_option=True)
    assert result == "Lines number: 2\nWords number: 6\nChars number: 21"


def test_empty_file(create_temp_file):
    file_path = create_temp_file("empty.txt", "")
    result = wc(file_path, l_option=True, w_option=True, c_option=True)
    assert result == "Lines number: 0\nWords number: 0\nChars number: 0"


def test_only_newlines(create_temp_file):
    file_path = create_temp_file("newlines.txt", "\n\n\n")
    result = wc(file_path, l_option=True, w_option=True, c_option=True)
    assert result == "Lines number: 3\nWords number: 0\nChars number: 0"


def test_special_characters(create_temp_file):
    file_path = create_temp_file("special.txt", "Hello, world!\n@#$%^&*()\n")
    result = wc(file_path, l_option=True, w_option=True, c_option=True)
    assert result == "Lines number: 2\nWords number: 3\nChars number: 21"


def test_no_options(create_temp_file):
    file_path = create_temp_file("test_no_options.txt", "Just a simple test.")
    result = wc(file_path)
    assert result == ""
