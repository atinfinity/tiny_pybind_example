import tiny_pybind_example2


def test_call(capfd):
    tiny_pybind_example2.call()
    out, __ = capfd.readouterr()
    assert out == '[testlib1] func1 is called.\n'
