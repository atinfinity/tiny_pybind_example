import tiny_pybind_example4
import pytest


def test_throws_out_of_range():
    with pytest.raises(IndexError):
        tiny_pybind_example4.throws_out_of_range()
