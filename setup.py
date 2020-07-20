# -*- coding: utf-8 -*-
"""Package configuration for setuptools."""

from setuptools import find_packages, setup

VERSION = "0.1"


def write_version_py(filename="demos_segmentation/version.py"):
    """Dynamically write App version file."""
    msg = "# This file is dynamically generated\n"
    version = f"version = '{VERSION}'"

    with open(filename, "w") as fd:
        fd.write(msg)
        fd.write("\n")
        fd.write(version)
        fd.write("\n")


setup(
    name="demos-segmentation",
    version=VERSION,
    description="DEMOS records segmentation",
    url="",
    author="demos@fit",
    author_email=["demos@fit.vutbr.cz",],
    install_requires=["Flask", "flask-restx", "opencv-python-headless",],
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.6",
)


if __name__ == "__main__":
    write_version_py()
