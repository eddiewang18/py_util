# setup.py

from setuptools import setup, find_packages

setup(
    name="py_util",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A utility package",
    author="Eddie Wang",
    author_email="",
    url="https://github.com/eddiewang18/py_util.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
