import tiny_pybind_example3
import numpy as np
import pytest


def test_add1d_int32():
    a = np.array([1, 2, 3], dtype=np.int32)
    b = np.array([1, 2, 3], dtype=np.int32)
    assert np.array_equal(tiny_pybind_example3.add1d(a, b), a + b)


def test_add1d_int32_shape_not_match():
    a = np.array([1, 2, 3], dtype=np.int32)
    b = np.array([1, 2], dtype=np.int32)
    with pytest.raises(RuntimeError):
        tiny_pybind_example3.add1d(a, b)


def test_add1d_int32_2d_input():
    a = np.array([[1, 2], [3, 4]], dtype=np.int32)
    b = np.array([[1, 2], [3, 4]], dtype=np.int32)
    with pytest.raises(RuntimeError):
        tiny_pybind_example3.add1d(a, b)


def test_add1d_float32():
    a = np.array([1.5, 2.5, 3.5], dtype=np.float32)
    b = np.array([1.5, 2.5, 3.5], dtype=np.float32)
    assert np.array_equal(tiny_pybind_example3.add1d(a, b), a + b)
