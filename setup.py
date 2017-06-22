from setuptools import setup
from setuptools import find_packages
import os
import pywc

currentFileDirectory = os.path.dirname(__file__)
with open(os.path.join(currentFileDirectory, "README.md"), "r") as f:
    readme = f.read()

print(find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]))

setup(
    name="pywc",
    version=pywc.VERSION,
    description="Count the number of words in a folder",
    long_description=readme,
    author="Alejandro Saucedo",
    author_email="a@e-x.io",
    url="https://github.com/axsauze/pywc",
    classifiers=[
        "Development Status :: 3 - Alpha Development Status"
        "Intended Audience :: Developers",
        "Programming Language :: Python 3",
        "Programming Language :: Python 3.2",
        "Programming Language :: Python 3.3",
    ],
    keywords="Word count (wc) on steroids",
    license="MIT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    scripts=('pywc.py',),
    data_files=[ (".", ["LICENSE"]) ],
    test_suite='tests'
)
