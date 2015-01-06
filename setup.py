from setuptools import setup

setup(name='pybib',
      version='1.0',
      description='Auto-generate a BibTeX file from a list of Digital Object Identifiers',
      url='https://github.com/jgilchrist/pybib',
      author='Jonny Gilchrist',
      packages=['pybib'],
      install_requires=[
          'requests',
      ],
      scripts=['bin/pybib'])
