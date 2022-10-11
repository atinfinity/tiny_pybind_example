import tiny_pybind_example5
import pytest


def test_func1_case1(capfd):
    tiny_pybind_example5.func1(i=2, j=3)
    out, __ = capfd.readouterr()
    assert out == 'i = 2, j = 3\n'


def test_func1_case2(capfd):
    tiny_pybind_example5.func1(j=2, i=3)
    out, __ = capfd.readouterr()
    assert out == 'i = 3, j = 2\n'


def test_func1_case3(capfd):
    tiny_pybind_example5.func1(2, 3)
    out, __ = capfd.readouterr()
    assert out == 'i = 2, j = 3\n'


def test_func1_incompatible_arg1():
    with pytest.raises(TypeError):
        tiny_pybind_example5.func1(2)


def test_func1_incompatible_arg2():
    with pytest.raises(TypeError):
        tiny_pybind_example5.func1()


def test_func1_incompatible_arg3():
    with pytest.raises(TypeError):
        tiny_pybind_example5.func1(k=1, l=2)


def test_func1_incompatible_arg4():
    with pytest.raises(TypeError):
        tiny_pybind_example5.func1(i=2.5, j=3.5)


def test_func2_case1(capfd):
    tiny_pybind_example5.func2()
    out, __ = capfd.readouterr()
    assert out == 'i = 0, j = 1\n'


def test_func2_case2(capfd):
    tiny_pybind_example5.func2(i=1)
    out, __ = capfd.readouterr()
    assert out == 'i = 1, j = 1\n'


def test_func2_case3(capfd):
    tiny_pybind_example5.func2(j=2)
    out, __ = capfd.readouterr()
    assert out == 'i = 0, j = 2\n'


def test_func2_case4(capfd):
    tiny_pybind_example5.func2(i=2, j=3)
    out, __ = capfd.readouterr()
    assert out == 'i = 2, j = 3\n'


def test_func2_case5(capfd):
    tiny_pybind_example5.func2(2, 3)
    out, __ = capfd.readouterr()
    assert out == 'i = 2, j = 3\n'


def test_func2_incompatible_arg1():
    with pytest.raises(TypeError):
        tiny_pybind_example5.func2(k=2)


def test_func2_incompatible_arg2():
    with pytest.raises(TypeError):
        tiny_pybind_example5.func2(i=2.5, j=3.5)
