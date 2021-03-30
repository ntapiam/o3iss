#!/usr/bin/env python3
import sys

from setuptools import setup
from setuptools_rust import RustExtension, Binding


setup(
    name="o3iss",
    version="0.1.1",
    rust_extensions=[RustExtension("o3iss.o3iss", binding=Binding.RustCPython)],
    packages=["o3iss"],
    zip_safe=False
)
