"""
See:
https://packaging.python.org/en/latest/distributing.html
"""
import os
from setuptools import setup

# To use a consistent encoding
from codecs import open

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sms-counter',
    version='1.0.0',
    description='SMS Character Counter',
    long_description=long_description,
    author='Dayo Ayeni',
    # author_email='',
    packages=['sms_counter'],
    install_requires=[""],
    include_package_data=True)
