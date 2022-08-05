# Copyright 2020 IBM Corporation
#
# Licensed under the GNU General Public License 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.gnu.org/licenses/gpl-3.0.txt
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
import os
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lale-autoai',
    version='0.1.0',
    author='IBM',
    description="Lale operators based on AutoAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IBM/lale-autoai",
    python_requires='>=3.8',
    packages=find_packages(),
    license='',
    install_requires=[
        'autoai-ts-libs>=1.1.12',
    ],
    extras_require={
        'full':[
            'javabridge>=1.0.18',
            'python-weka-wrapper3>=0.1.7',
            'rpy2>=3.0.2',
            'platypus-opt>=1.0.4'
        ],
        'test':[
            'jupyter',
            'mypy',
            'flake8',
            "sphinx==2.4.4",
            "m2r2",
            "sphinx_rtd_theme",
            "sphinxcontrib.apidoc"
        ]}
)
