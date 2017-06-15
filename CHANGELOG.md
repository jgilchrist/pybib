# Change Log

All notable changes to this project will be documented in this file.
This project loosely adheres to [Semantic Versioning](http://semver.org/).

<!--
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
-->

## [Unreleased][x.x.x]

## [2.2.2]
### Fixed
- Fixed Unicode encoding issues in Python 2.x

## [2.2.1]
### Fixed
- Stopped using the deprecated 'scripts' in setup.py, preferring 'entry_points'

## [2.2.0]
### Added
- pybib is now fully compatible with Python 2.x
- The project now has an in-repository changelog.

### Changed
- pybib is now licensed under the 3-clause BSD license.

### Fixed
- Fixed a case where different versions of argparse could cause subcommands to
  fail to override the parent command's default for a value, which could cause
  no commands to be run.
- Absence of a title for any entry is now handled gracefully.
- A case of termstyle.auto() intefering with nosetests output has been rectified.
- Prefer sys.exit() over exit().

## [2.1.0]
### Added
- When searching, each result now shows its type (e.g. Book chapter, Journal article) in addition to its other information
- The project was licensed under GNU v3

### Changed
- The number of search results has been limited to 10 so that they are more likely to fit in a terminal window

## [2.0.1]
### Fixed
- Rerelease of 2.0.0 which ensures that PyPi uses the README as the package description.

## [2.0.0]
### Added

- The command line interface has been changed to use subcommands
  To use the tool like before, use bib get instead of bib
- The bib search command has been added, which gets a list of resources matching a search term
  After getting a list, the citation for any particular result can be obtained by passing the --get argument

## [1.3.0]
### Removed

- The ability to generate a .bib file from a .doi file has been removed.
  If you need this ability, use an earlier version (< 1.3.0).

## [1.2.2]
### Fixed
- Some valid DOIs were not being recognised as such.
- The `-o` flag for outputting to a file was not writing to the correct filename.

## [1.2.1]
### Fixed
- Fixes installation from PyPI.

## [1.2.0]
### Changed
- The default behaviour of the program is now retrieving a single DOI.
  This allows the following behaviour:

  `$ bib doi123 >> citations.bib`

  To get the old behaviour:

  `$ bib -f citations.doi > citations.bib`
- Most of the output is now hidden behind a flag (-v or --verbose)
- Identifiers for DOIs no longer have a length limit.

### Fixed
- Identifiers for DOIs were not allowed to be alphanumeric.
- Spaces in BibTeX keys could not be replaced.

## [1.1.0]
### Changed
- Improved progress notifications.

### Fixed
- Some DOIs which should've be recognised as valid didn't match the previous DOI regular expression.
- The entire program would run if the file was empty.

## 1.0.0
- Initial release.

[x.x.x]: https://github.com/jgilchrist/pybib/compare/v2.2.2...HEAD
[2.2.2]: https://github.com/jgilchrist/pybib/compare/v2.2.1...v2.2.2
[2.2.1]: https://github.com/jgilchrist/pybib/compare/v2.2.0...v2.2.1
[2.2.0]: https://github.com/jgilchrist/pybib/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/jgilchrist/pybib/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/jgilchrist/pybib/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/jgilchrist/pybib/compare/v1.3.0...v2.0.0
[1.3.0]: https://github.com/jgilchrist/pybib/compare/v1.2.2...v1.3.0
[1.2.2]: https://github.com/jgilchrist/pybib/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/jgilchrist/pybib/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/jgilchrist/pybib/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jgilchrist/pybib/compare/v1.0.0...v1.1.0
