import pytest

from main import run_1, run_2
from utils import read_instructions

INPUT_FILE_NAME: str = "input.txt"


@pytest.fixture
def given_input_file():
    return read_instructions(INPUT_FILE_NAME)


def test_input_file_ok_1(given_input_file):
    result = run_1(given_input_file)

    expected_result = 1071

    assert result == expected_result


def test_input_file_ok_2(given_input_file):
    result = run_2(given_input_file)

    expected_result = 6700

    assert result == expected_result
