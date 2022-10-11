# Example2: Module links self library

## Install package

```shell
git clone https://github.com/atinfinity/tiny_pybind_example.git
cd tiny_pybind_example/tiny_pybind_example2
pip3 install -e .
```

## Example

```python
import tiny_pybind_example2
tiny_pybind_example2.call()
```

## Test

```shell
pytest -v tests
```

Please see [tests](tests).
