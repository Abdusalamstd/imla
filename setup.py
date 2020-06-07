# encoding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yeziq-Abduroid", # Replace with your own username
    version="0.0.1",
    author="Abdusalam",
    author_email="Abdusalam123456@163.com",
    description="A small package that process Uyghur letters and chars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
     license = "MIT Licence",
    
    url="https://github.com/Abdusalamstd/yeziq/",
    packages=setuptools.find_packages(),
    platforms = "any",
    install_requires = [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
