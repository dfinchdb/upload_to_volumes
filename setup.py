"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the upload_to_volumes project.
"""
from setuptools import setup, find_packages

import sys

sys.path.append("./src")

import upload_to_volumes

setup(
    name="upload_to_volumes",
    version=upload_to_volumes.__version__,
    url="https://databricks.com",
    author="david.finch@databricks.com",
    description="wheel file based on upload_to_volumes/src",
    packages=find_packages(where="./src"),
    package_dir={"": "src"},
    entry_points={"packages": ["volumes=upload_to_volumes.upload_files:upload_dir"]},
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
