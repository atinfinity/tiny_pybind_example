#include "testlib1.h"
#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

void call() {
    func1();
}

namespace py = pybind11;

PYBIND11_MODULE(tiny_pybind_example2, m) {
    m.doc() = "tiny pybind example module";
    m.def("call", &call, "call func2()");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
