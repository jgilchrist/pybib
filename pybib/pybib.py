import re
import os
import sys
import requests

# Matches a valid DOI
doi_matcher = re.compile('\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')

# Matches a [citation_key DOI] pair
key_file_matcher = re.compile('(\S+)\s+(\S+)')

# Matches the beginning of a BibTeX entry
bibtex_key_matcher = re.compile('@\w+{(.+?),')


def convert_file(filename, driver, out_to_file, verbose):
    """Convert a file in the format [citation_key doi_key]* into a valid bibtex file"""

    if verbose:
        print("Retrieving entries from {}".format(driver.url))

    doi_entries = parse_file(filename, verbose)

    bib_entries = get_all_bibliography_data(doi_entries, driver, verbose)

    bib_entries = replace_citation_keys(bib_entries)

    writefn = write_to_file if out_to_file else write_to_stdout

    writefn(bib_entries, filename, verbose)

def write_to_file(entries, filename, verbose):
    (root, ext) = os.path.splitext(filename)
    bibtex_file = root + ".bib"

    with open(bibtex_file, 'w') as bib:
        for citation in entries:
            print(citation, file=bib)

    if verbose:
        print("Wrote generated BibTeX file as {}".format(bibtex_file))

def write_to_stdout(entries, filename, verbose):
    for citation in entries:
        print(citation)

def parse_file(filename, verbose):
    """Parses a file in the format [citation_key doi_key]* into a dictionary {citation_key: doi_key}*"""

    doi_entries = {}

    with open(filename) as f:
        lines = f.readlines()

    for i, line in enumerate(lines, start=1):

        parsed_line = parse_line(i, line)

        if parsed_line is None:
            # Line was blank, or a comment
            continue

        citation_key, doi = parsed_line

        # Don't allow duplicate citation keys
        if citation_key in doi_entries:
            error("Line {}: duplicate citation key: {}".format(i, citation_key))

        doi_entries[citation_key] = doi

    if verbose:
        print("Found {} citations in {}".format(len(doi_entries), filename))

    if not doi_entries:
        error("Nothing to do")

    return doi_entries

def parse_line(line_number, line):
    """Parses a single line, of the format [citation_key DOI]"""

    if line.isspace():
        return None

    if line.startswith("#"):
        # Found a comment
        return None

    parsed_line = key_file_matcher.match(line)

    if not parsed_line:
        error("Line {}: Syntax error ({})".format(line_number, line.strip()))

    citation_key, doi = parsed_line.group(1, 2)

    if not doi_matcher.match(doi):
        error("Line {}: Invalid DOI {}".format(line_number, doi))

    return citation_key, doi

def get_all_bibliography_data(doi_entries, driver, verbose):
    """Takes a dict in the format {citation_key: doi_key}* and expands each doi key into its bibliography text"""

    if verbose:
        print("Retrieving bibliography entries:")

    key_to_bibliography = {}

    for citation_key, doi in doi_entries.items():
        if verbose:
            print("\t{} ({}) -> ".format(citation_key, doi), end="")
        bibliography_text = driver.get_entry(doi)
        if verbose:
            print("Done.")

        key_to_bibliography[citation_key] = bibliography_text

    return key_to_bibliography


def replace_citation_keys(key_to_bibliography):
    """Single the bibtex entry comes with a default citation key, we need to replace
    this with the key specified in the file"""

    return [replace_key(entry, key) for (entry, key) in key_to_bibliography]


def replace_key(entry, key):
    citation_key_match = bibtex_key_matcher.match(entry)

    if not citation_key_match:
        error("Ill formatted bibtex entry:\n{}".format(bib_text))

    old_key = citation_key_match.group(1)

    new_entry = entry.replace(old_key, key)

    return new_entry


def error(msg):
    sys.exit(msg)
