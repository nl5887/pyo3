from setuptools import setup
from setuptools_rust import RustExtension

setup(
    rust_extensions=[RustExtension("setuptools_rust_starter._setuptools_rust_starter")],
)
