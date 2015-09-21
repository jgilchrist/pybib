pybib |PyPI version| |Travis CI| |Codecov| |Code Climate|
===========================================================

pybib is a super-easy way to get citations for your LaTeX document.
Instead of typing out BibTeX entries yourself, just give pybib the
Digital Object Identifier (DOI) of the resource you want to cite and it
will get all the information for you. Then, you can just add the
citation it gives you to your BibTeX file. Easy!

Demo
----

|demo|

Installation
------------

The package is available on PyPi and can be installed with the following
command:

.. code:: sh

    $ pip3 install --user pybib

For user-only installs, pip installs scripts to the directory
``~/.local/bin``, so make sure it’s in your path. If you would prefer to
install it system-wide, just leave out the ``--user`` flag.

Usage examples
--------------

Get a citation:

.. code:: sh

    $ bib get 10.1112/plms/s2-42.1.230

Get a citation and add it to your bibliography file:

.. code:: sh

    $ bib get 10.1145/159544.159617 >> citations.bib

Get a citation and add it to your bibliography file, running it through
``bibtool`` first to format the entry and auto-generate a citation key:

.. code:: sh

    $ bib get 10.1145/159544.159617 | bibtool >> citations.bib

Searching
---------

Search for a resource:

.. code:: sh

    $ bib search name of the resource

Get the citation for search result number ``N``:

.. code:: sh

    $ bib search name of the resource --get N

Troubleshooting
---------------

If you encounter any problems, please open an issue so I can rectify
them as soon as possible.

.. |demo| image:: https://asciinema.org/a/d28uzeuzswvbzvd1itd5gd1gi.png
   :target: https://asciinema.org/a/d28uzeuzswvbzvd1itd5gd1gi?autoplay=1
.. |PyPI version| image:: https://img.shields.io/pypi/v/pybib.svg?style=flat
   :target: https://pypi.python.org/pypi?:action=display&name=pybib
.. |Travis CI| image:: https://travis-ci.org/jgilchrist/pybib.svg?branch=master
    :target: https://travis-ci.org/jgilchrist/pybib
.. |Codecov| image:: http://codecov.io/github/jgilchrist/pybib/coverage.svg?branch=master
   :target: http://codecov.io/github/jgilchrist/pybib?branch=master
.. |Code Climate| image:: https://codeclimate.com/github/jgilchrist/pybib/badges/gpa.svg
   :target: https://codeclimate.com/github/jgilchrist/pybib
