import tiny_pybind_example1


def test_add():
    assert tiny_pybind_example1.add(1, 2) == 3

def test_sub():
    assert tiny_pybind_example1.sub(1, 2) == -1
