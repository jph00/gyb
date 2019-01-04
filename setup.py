from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f: long_description = f.read()

setup(
    name='gyb',
    version='1.0.2',
    description="Apple gyb, a simple python-based templating tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jph00/gyb',
    author='Apple (pip packaged by Jeremy Howard)',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='development',
    py_modules=["gyb", "linedirective"],
    entry_points={ 'console_scripts': [ 'gyb=gyb:main', 'line-directive=linedirective:main' ] }
)

