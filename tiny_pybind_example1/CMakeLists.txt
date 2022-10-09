cmake_minimum_required(VERSION 3.4...3.18)
project(tiny_pybind_example1)

find_package(pybind11 REQUIRED)
pybind11_add_module(${PROJECT_NAME} src/module.cpp)

# PACKAGE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${PACKAGE_VERSION_INFO})
