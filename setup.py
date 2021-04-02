from setuptools import setup
from setuptools_rust import RustExtension, Binding
setup(
    name="iss",
    author="Nikolas Tapia",
    author_email="tapia@wias-berlin.de",
    version="0.1.2",
    packages=["iss"],
    zip_safe=False,
    url="https://github.com/ntapiam/o3iss",
    rust_extensions=[RustExtension("iss.o3iss", binding=Binding.RustCPython)]
)
