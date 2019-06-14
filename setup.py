

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="gc2d-rug",
    version="0.0.1",
    author="University of Groningen (RUG) 2D-GC team",
    description="3D visualisation for GCxGC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GeorgeArgyrousisUni/2D-GC",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "PyOpenGL",
        "PyQt5",
        "PyQt5-sip",
        "pyqtgraph",
        "scipy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)
