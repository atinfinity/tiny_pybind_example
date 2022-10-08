#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <cstdint>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

template <typename T>
py::array_t<T> add1d(py::array_t<T> input1, py::array_t<T> input2) {
    py::buffer_info buf1 = input1.request(), buf2 = input2.request();
    if (buf1.ndim != 1 || buf2.ndim != 1) {
        throw std::runtime_error("Number of dimensions must be one");
    }
    if (buf1.size != buf2.size) {
        throw std::runtime_error("Input shapes must match");
    }

    auto result = py::array_t<T>(buf1.shape);
    py::buffer_info buf3 = result.request();

    T *ptr1 = static_cast<T *>(buf1.ptr);
    T *ptr2 = static_cast<T *>(buf2.ptr);
    T *ptr3 = static_cast<T *>(buf3.ptr);

    for (size_t idx = 0; idx < buf1.shape[0]; idx++) {
        ptr3[idx] = ptr1[idx] + ptr2[idx];
    }

    return result;
}

PYBIND11_MODULE(tiny_pybind_example3, m) {
    m.doc() = "tiny pybind example module";
    m.def("add1d", &add1d<std::int8_t>, "Add two NumPy arrays");
    m.def("add1d", &add1d<std::int16_t>, "Add two NumPy arrays");
    m.def("add1d", &add1d<std::int32_t>, "Add two NumPy arrays");
    m.def("add1d", &add1d<std::int64_t>, "Add two NumPy arrays");

    m.def("add1d", &add1d<std::uint8_t>, "Add two NumPy arrays");
    m.def("add1d", &add1d<std::uint16_t>, "Add two NumPy arrays");
    m.def("add1d", &add1d<std::uint32_t>, "Add two NumPy arrays");
    m.def("add1d", &add1d<std::uint64_t>, "Add two NumPy arrays");

    m.def("add1d", &add1d<float>, "Add two NumPy arrays");
    m.def("add1d", &add1d<double>, "Add two NumPy arrays");
    m.def("add1d", &add1d<long double>, "Add two NumPy arrays");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
