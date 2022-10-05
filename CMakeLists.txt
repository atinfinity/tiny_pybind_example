cmake_minimum_required(VERSION 3.4...3.18)
project(tiny_pybind_example)

find_package(pybind11)
pybind11_add_module(tiny_pybind_example src/module.cpp)

# PACKAGE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(tiny_pybind_example PRIVATE VERSION_INFO=${PACKAGE_VERSION_INFO})
