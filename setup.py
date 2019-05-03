from setuptools import find_packages, setup

setup(
    name='2D-GC',
    version='0.1',
    packages=find_packages(),
    scripts=['scripts/gc2d'],
    description='2d-gc visualiser',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy==1.16.2",
        "PyOpenGL==3.1.0",
        "PyQt5==5.12.1",
        "PyQt5-sip==4.19.15"
    ],
    dependency_links=['https://github.com/pyqtgraph/pyqtgraph/tarball/master']
)