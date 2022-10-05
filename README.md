# tiny_pybind_example

## Introduction

The <https://github.com/pybind/cmake_example> is example of pybind11 with a CMake-based build system.  
`tiny_pybind_example` is a simplified version of BBB for learning.

## Requirements

- CMake
- build-essential
- python3-dev
- python3-pip
- python3-pybind11

## Usage

```shell
https://github.com/atinfinity/tiny_pybind_example.git
cd tiny_pybind_example
pip3 install -e .
```

## Test

```python
import tiny_pybind_example
tiny_pybind_example.add(1, 2)
tiny_pybind_example.sub(1, 2)
```