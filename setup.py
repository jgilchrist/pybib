from setuptools import setup

from pybib import __version__

setup(name='pybib',
      version=__version__,
      description='Fetch citation information, given a Digital Object Identifier',
      long_description=open('README.rst').read(),
      url='https://github.com/jgilchrist/pybib',
      author='Jonny Gilchrist',
      packages=['pybib'],
      install_requires=[
          'requests',
          'python-termstyle',
      ],
      scripts=['bin/bib'])
