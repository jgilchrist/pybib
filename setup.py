from setuptools import setup, find_packages

from pybib import __version__

with open('README.rst') as f:
    readme = f.read()

setup(name='pybib',
    version=__version__,
    description='Fetch citation information, given a Digital Object Identifier',
    long_description=readme,
    url='https://github.com/jgilchrist/pybib',
    author='Jonathan Gilchrist',
    license='BSD 3-Clause License',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama'
    ],
    entry_points = {
        'console_scripts': [
            'bib = pybib:main'
        ]
    }
)
