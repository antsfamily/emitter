#!/usr/bin/env python
# Copyright (c) 2019-2021, Zhi Liu.  All rights reserved.

from setuptools import setup
from setuptools import find_packages


setup(name='emitter',
      version='1.0.0',
      description="Radar Emitter Signal Simulation, Sorting and Recognition",
      author='Zhi Liu',
      author_email='zhiliu.mind@gmail.com',
      url='https://iridescent.ink/emitter',
      download_url='https://github.com/emitter',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'lxml',
          'numpy',
          'matplotlib',
          'scipy',
          'h5py',
      ],
      extras_require={
          'h5py': ['h5py'],
          'visualize': ['pydot>=1.2.0'],
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'pytest-cov'],
      },
      keywords=[
          'emitter',
          'radar',
          'sorting',
          'simulation'
      ]
      )
