import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tempenviron",
    version="0.0.1",
    author="u1234x1234",
    author_email="u1234x1234@gmail.com",
    description=(""),
    license="MIT",
    keywords="",
    url="https://github.com/u1234x1234/tempenviron",
    packages=['tempenviron'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
) 
