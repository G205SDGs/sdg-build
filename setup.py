# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='sdg',
      version='0.1.0',
      description='Build SDG data and metadata into output formats',
      url='https://github.com/mangothecat/sdg-build',
      author='Doug Ashton',
      author_email='douglas.j.ashton@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'check', 'reset']),
      zip_safe=False,
      install_requires=['pyyaml', 'gitpython', 'pandas', 'yamlmd'],
      dependency_links=[
        "git+ssh://git@github.com/dougmet/yamlmd.git@0.1.7"
    ])