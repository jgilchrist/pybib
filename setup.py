from setuptools import setup

setup(name='pybib',
      version='1.3.0',
      description='Fetch citation information, given a Digital Object Identifier',
      url='https://github.com/jgilchrist/pybib',
      author='Jonny Gilchrist',
      packages=['pybib'],
      install_requires=[
          'requests',
      ],
      scripts=['bin/bib'])
