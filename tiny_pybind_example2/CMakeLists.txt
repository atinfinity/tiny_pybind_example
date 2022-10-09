cmake_minimum_required(VERSION 3.4...3.18)
project(tiny_pybind_example2)

add_subdirectory(testlib1)

find_package(pybind11 REQUIRED)
pybind11_add_module(${PROJECT_NAME} src/module.cpp)

include_directories(testlib1/include)
target_link_libraries(${PROJECT_NAME} PRIVATE pybind11::module testlib1)

# PACKAGE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${PACKAGE_VERSION_INFO})
