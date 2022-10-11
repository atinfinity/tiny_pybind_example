#include <pybind11/pybind11.h>
#include <iostream>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

void func1(int i, int j) {
    std::cout << "i = " << i << ", j = " << j << std::endl;
}

void func2(int i=0, int j=1) {
    std::cout << "i = " << i << ", j = " << j << std::endl;
}

PYBIND11_MODULE(tiny_pybind_example5, m) {
    m.doc() = "tiny pybind example module";
    m.def("func1", &func1, "Example of keyword arguments", py::arg("i"), py::arg("j"));
    m.def("func2", &func2, "Example of keyword arguments(has default value)", py::arg("i") = 0, py::arg("j") = 1);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
