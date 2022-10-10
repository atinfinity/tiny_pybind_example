# Example1: Minimum example

## Install package

```shell
git clone https://github.com/atinfinity/tiny_pybind_example.git
cd tiny_pybind_example/tiny_pybind_example1
pip3 install -e .
```

## Example

```python
import tiny_pybind_example1
tiny_pybind_example1.add(1, 2)
tiny_pybind_example1.sub(1, 2)
```

## Test

```shell
pytest -v tests
```

Please see [tests](tests).
