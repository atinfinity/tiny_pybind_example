#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(tiny_pybind_example1, m) {
    m.doc() = "tiny pybind example module";
    m.def("add", &add, "Add two numbers");
    m.def("sub", [](int i, int j) { return i - j; }, "Subtract two numbers");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
