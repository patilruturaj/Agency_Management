# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in agency_management/__init__.py
from agency_management import __version__ as version

setup(
	name='agency_management',
	version=version,
	description='This is Car Agency Management System.',
	author='Ruturaj Patil',
	author_email='patilruturaj31098@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
