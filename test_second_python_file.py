import pytest
import second_python_file

def test_this_test_should_fail():
    assert second_python_file.multiply_n_numbers([1, 2, 3]) != 7

def test_this_test_should_pass():
    assert second_python_file.multiply_n_numbers([1, 2, 4]) == 8

def test_check_zero_values():
    assert second_python_file.multiply_n_numbers([0, 1]) == 0

def test_having_string():
    assert second_python_file.multiply_n_numbers([1, 3, "n"]) == "nnn"
    