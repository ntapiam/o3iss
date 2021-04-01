from setuptools import setup
from setuptools_rust import RustExtension, Binding


setup(
    packages = ["o3iss"],
    rust_extensions = [RustExtension("o3iss.o3iss", binding=Binding.RustCPython)]
)

