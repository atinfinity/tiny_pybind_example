# Example5: Uses keyword arguments

## Install package

```shell
git clone https://github.com/atinfinity/tiny_pybind_example.git
cd tiny_pybind_example/tiny_pybind_example5
pip3 install -e .
```

## Example

```python
import tiny_pybind_example5

tiny_pybind_example5.func1(i=2, j=3)
tiny_pybind_example5.func2()
```

## Test

```shell
pytest -v tests
```

Please see [tests](tests).

## Reference

- <https://pybind11.readthedocs.io/en/stable/basics.html#keyword-arguments>
- <https://pybind11.readthedocs.io/en/stable/basics.html#default-arguments>
