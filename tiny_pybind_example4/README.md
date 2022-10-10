# Example4: Handle C++ exception

## Install package

```shell
git clone https://github.com/atinfinity/tiny_pybind_example.git
cd tiny_pybind_example/tiny_pybind_example4
pip3 install -e .
```

## Example

```python
import tiny_pybind_example4
import traceback

try:
    tiny_pybind_example4.throws_out_of_range()
except:
    print(traceback.format_exc())
```

## Test

```shell
pytest -v tests
```

Please see [tests](tests).

## Reference

- <https://pybind11.readthedocs.io/en/stable/advanced/exceptions.html>
