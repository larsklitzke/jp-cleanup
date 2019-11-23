# -*- coding: utf-8 -*-
# Copyright (c) 2019 by Lars Klitzke, Lars.Klitzke@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os

from setuptools import setup, find_packages

setup(
    name='jp-cleanup',
    version='0.0.0',
    description='Cleanup Jupyter Notebook files',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    author='Lars Klitzke',
    author_email='Lars.Klitzke@gmail.com',
    license="GNU GPLv3",
    packages=find_packages(),
    install_requires=open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).readlines(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Unix Shell',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Manufacturing',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'jp-cleanup=jpcleanup:main'
        ]
    }
)
