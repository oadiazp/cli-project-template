#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name='{{ cookiecutter.project_name }}',
    version='1.0.1',
    description='Lendable parsing tool',
    author='Omar Diaz',
    author_email='{{ cookiecutter.project_owner }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'Click',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_name }}={{ cookiecutter.project_name }}:tool',
        ]
    },
)
