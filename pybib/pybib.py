import logging
import re
import os
import sys
import requests

from .drivers import DriverResult

# Matches a [citation_key DOI] pair
key_file_matcher = re.compile('(\S+)\s+(\S+)')

# Matches the beginning of a BibTeX entry
bibtex_key_matcher = re.compile('@\w+{(.+?),')


def convert_file(filename, driver, out_to_file):
    """Convert a file in the format [citation_key doi_key]* into a valid bibtex file"""

    logging.info("Retrieving entries from {}".format(driver.url))

    doi_entries = parse_file(filename)

    bib_entries = get_all_bibliography_data(doi_entries, driver)

    bib_entries = replace_citation_keys(bib_entries)

    writefn = write_to_file if out_to_file else write_to_stdout

    writefn(bib_entries, filename, out_to_file)

def write_to_file(entries, filename, out_to_file):
    bibtex_file = out_to_file

    with open(bibtex_file, 'w') as bib:
        for citation in entries:
            print(citation, file=bib)

    logging.info("Wrote generated BibTeX file as {}".format(bibtex_file))

def write_to_stdout(entries, filename, out_to_file):
    for citation in entries:
        print(citation)

def parse_file(filename):
    """Parses a file in the format [citation_key doi_key]* into a dictionary {citation_key: doi_key}*"""

    doi_entries = {}

    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError as e:
        error('File not found: {}'.format(e.filename))

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

    logging.info("Found {} citations in {}".format(len(doi_entries), filename))

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

    return citation_key, doi

def get_all_bibliography_data(doi_entries, driver):
    """Takes a dict in the format {citation_key: doi_key}* and expands each doi key into its bibliography text"""

    logging.info("Retrieving bibliography entries:")

    key_to_bibliography = {}

    for citation_key, doi in doi_entries.items():
        logging.info("\t{} -> ({})".format(citation_key, doi, end=""))
        (status, output) = driver.get_entry(doi)

        if status == DriverResult.unknown:
            print('Unknown DOI with citation key "{}": {}'.format(citation_key, doi))
            sys.exit(1)

        bibliography_text = output

        logging.info("Done.")

        key_to_bibliography[citation_key] = bibliography_text

    return key_to_bibliography


def replace_citation_keys(key_to_bibliography):
    """Single the bibtex entry comes with a default citation key, we need to replace
    this with the key specified in the file"""

    return [replace_key(key, entry) for (key, entry) in key_to_bibliography.items()]


def replace_key(key, entry):
    citation_key_match = bibtex_key_matcher.match(entry)

    if not citation_key_match:
        error("Ill formatted bibtex entry:\n{}".format(entry))

    old_key = citation_key_match.group(1)

    new_entry = entry.replace(old_key, key)

    return new_entry


def error(msg):
    sys.exit(msg)
