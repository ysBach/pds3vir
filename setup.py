"""
"""

from setuptools import setup, find_packages

setup_requires = []
install_requires = ['numpy', "pvl", "six", "astropy"]

classifiers = ["Intended Audience :: Science/Research",
               "Operating System :: OS Independent",
               "Programming Language :: Python :: 3.8",
               ]

setup(
    name="pds3vir",
    version="0.1.dev",
    author="Yoonsoo P. Bach",
    author_email="ysbach93@gmail.com",
    description="",
    license="BSD3",
    keywords="",
    url="https://github.com/ysBach/ysvisutilpy",
    classifiers=classifiers,
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=install_requires)
