import tiny_pybind_example3
import numpy as np

a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1, 2, 3], dtype=np.int32)
c = tiny_pybind_example3.add1d(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"verify(np.int32) = {np.array_equal(c, a + b)}\n")

d = np.array([1.5, 2.5, 3.5], dtype=np.float32)
e = np.array([1.5, 2.5, 3.5], dtype=np.float32)
f = tiny_pybind_example3.add1d(d, e)
print(f"d = {d}")
print(f"e = {e}")
print(f"f = {f}")
print(f"verify(np.float32) = {np.array_equal(f, d + e)}")
