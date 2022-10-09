import tiny_pybind_example4
import traceback

try:
    tiny_pybind_example4.throws_out_of_range()
except:
    print(traceback.format_exc())
