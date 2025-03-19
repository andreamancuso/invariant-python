from setuptools import setup, Extension

module = Extension("invariant_python", sources=["invariant_python.c"])

setup(
    name="invariant_python",
    version="0.1",
    description="A native Python extension enforcing Design by Contract (DbC) invariants.",
    ext_modules=[module],
)
