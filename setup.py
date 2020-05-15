#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Maksym Novozhylov",
    author_email="mnovozhilov@upwork.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Python bindings for Upwork API",
    entry_points={"console_scripts": ["upwork=upwork.cli:main"]},
    install_requires=["requests_oauthlib>=1.3.0"],
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"upwork": ["py.typed"]},
    include_package_data=True,
    keywords="python-upwork",
    name="python-upwork",
    package_dir={"": "src"},
    packages=find_packages(include=["src/upwork", "src/upwork.*"]),
    setup_requires=[],
    url="https://github.com/upwork/python-upwork",
    version="2.0.0",
    zip_safe=False,
)
