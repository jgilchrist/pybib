from setuptools import setup

from pybib import __version__

with open('README.rst') as f:
    readme = f.read()

setup(name='pybib',
      version=__version__,
      description='Fetch citation information, given a Digital Object Identifier',
      long_description=readme,
      url='https://github.com/jgilchrist/pybib',
      author='Jonny Gilchrist',
      packages=['pybib'],
      install_requires=[
          'requests',
          'python-termstyle',
      ],
      entry_points = {
          'console_scripts': [
              'bib = pybib:main'
          ]
      }
)
