# pybib [![PyPI version](https://img.shields.io/pypi/v/pybib.svg?style=flat)](https://pypi.python.org/pypi?:action=display&name=pybib)

pybib is a super-easy way to get citations for your LaTeX document. Instead of typing out BibTeX entries yourself, just give pybib the Digital Object Identifier (DOI) of the resource you want to cite and it will get all the information for you. Then, you can just add the citation it gives you to your BibTeX file. Easy!

## Installation

The package is available on PyPi and can be installed with the following command:

```sh
$ pip3 install --user pybib
```

For user-only installs, pip installs scripts to the directory `~/.local/bin`, so make sure it's in your path. If you would prefer to install it system-wide, just leave out the `--user` flag.

## Usage examples

Get a citation:

```sh
$ bib 10.1112/plms/s2-42.1.230
```

Get a citation and add it to your bibliography file:

```sh
$ bib 10.1145/159544.159617 >> citations.bib
```

Get a citation and add it to your bibliography file, running it through `bibtool` first to format the entry and auto-generate a citation key:

```sh
$ bib 10.1145/159544.159617 | bibtool >> citations.bib
```

## Troubleshooting

If you encounter any problems, please open an issue so I can rectify them as soon as possible.
