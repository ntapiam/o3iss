from setuptools import setup
from setuptools_rust import RustExtension, Binding
setup(
    rust_extensions=[RustExtension("iss.o3iss", binding=Binding.RustCPython)]
)
