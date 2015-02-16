# pybib [![PyPI version](https://img.shields.io/pypi/v/pybib.svg?style=flat)](https://pypi.python.org/pypi?:action=display&name=pybib)

## Installation

To use this script, install the package using `pip` with the following command:

```sh
$ pip3 install --user pybib
```

For user-only installs, pip installs scripts to the directory `~/.local/bin`, so make sure it's in your path.

## Usage examples

Retrieve a single citation:

```sh
$ bib 10.1112/plms/s2-42.1.230

@article{Turing_1937,
    doi = {10.1112/plms/s2-42.1.230},
    url = {http://dx.doi.org/10.1112/plms/s2-42.1.230},
    year = 1937,
    month = {jan},
    publisher = {Oxford University Press ({OUP})},
    volume = {s2-42},
    number = {1},
    pages = {230--265},
    author = {A. M. Turing},
    title = {On Computable Numbers, with an Application to the Entscheidungsproblem},
    journal = {Proceedings of the London Mathematical Society}
}
```

Retrieve a single citation and add it to a bibliography file:

```sh
$ bib 10.1145/159544.159617 >> citations.bib
```

Retrieve a single citation and add it to a bibliography file, running it through `bibtool` first to format the entry and auto-generate a citation key:

```sh
$ bib 10.1145/159544.159617 | bibtool >> citations.bib
```

Convert a file containing a list of DOIs into a bibliography file:

```
$ bib -f citations.doi
```

## Troubleshooting

If you encounter problems using this program, please open an issue on this repository so I can rectify the problem.
