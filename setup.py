#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, office-microbes development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

__version__ = "0.0.0-dev"

import os
from setuptools import find_packages, setup
from setuptools.extension import Extension

classes = """
    Development Status :: 1 - Planning
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python
    Programming Language :: Python :: 3.4
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = ('Notebooks and code for our Sloan office microbiome project.')

setup(name='office-microbes',
      version=__version__,
      license='BSD',
      description=description,
      long_description=description,
      author="https://github.com/gregcaporaso/office-microbes/graphs/contributors",
      author_email="gregcaporaso@gmail.com",
      maintainer="https://github.com/gregcaporaso/office-microbes/graphs/contributors",
      maintainer_email="gregcaporaso@gmail.com",
      url='https://github.com/gregcaporaso/office-microbes',
      test_suite='nose.collector',
      packages=find_packages(),
      install_requires=['scikit-bio >= 0.4.0, < 0.5.0',
                        'ipython >= 3.1.0, < 4.0.0',
                        'seaborn'],
      extras_require={'test': ["nose >= 0.10.1"]},
      classifiers=classifiers,
      package_data={}
      )
