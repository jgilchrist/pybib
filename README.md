# pybib

This script takes a file with a list of digital object identifiers, and auto-generates a BibTeX file with the relevant information.

Example input:

```
network_failures        10.1145/2043164.2018477
comp_sci_ubiq           10.1145/159544.159617
```

Example output:

```
@article{network_failures, title={Understanding network failures in data centers}, volume={41}, ISSN={0146-4833}, url={http://dx.doi.org/10.1145/2043164.2018477}, DOI={10.1145/2043164.2018477}, number={4}, journal={ACM SIGCOMM Computer Communication Review}, publisher={Association for Computing Machinery (ACM)}, author={Gill, Phillipa and Jain, Navendu and Nagappan, Nachiappan}, year={2011}, month={Oct}, pages={350}}
@article{comp_sci_ubiq, title={Some computer science issues in ubiquitous computing}, volume={36}, ISSN={0001-0782}, url={http://dx.doi.org/10.1145/159544.159617}, DOI={10.1145/159544.159617}, number={7}, journal={Communications of the ACM}, publisher={Association for Computing Machinery (ACM)}, author={Weiser, Mark}, year={1993}, month={Jul}, pages={75–84}}
```

## Installation

To use this script, install the package using `pip` with the following command:

```
pip install --user pybib
```

## Troubleshooting

If you encounter problems using this program, please open an issue on this repository so I can rectify the problem.
