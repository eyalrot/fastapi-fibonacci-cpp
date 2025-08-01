from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

ext_modules = [
    Pybind11Extension(
        "fibonacci_cpp",
        ["cpp_math/fibonacci.cpp"],
        include_dirs=["cpp_math"],
        cxx_std=11,
    ),
]

setup(
    name="fibonacci_cpp",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
