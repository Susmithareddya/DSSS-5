from distutils.core import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='1.0.0',
    packages=['snowflake'],
    package = find_packages(),
    install_requires = ["numpy","turtles"],
    url='',
    license='',
    author='arumalla',
    author_email='susmithar456@gmail.com',
    description='setup of snowflake'
)
