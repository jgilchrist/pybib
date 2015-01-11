import re
import os
import sys
import requests

# Matches a valid DOI
doi_matcher = re.compile('\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b')

# Matches a [citation_key DOI] pair
key_file_matcher = re.compile('(\w+)\s+(\S+)')

# Matches the beginning of a BibTeX entry
bibtex_key_matcher = re.compile('@\w+{(\w+),')


def convert_file(filename, driver):
    """Convert a file in the format [citation_key doi_key]* into a valid bibtex file"""

    print("Retrieving entries from {}".format(driver.url))

    doi_entries = parse_file(filename)

    bib_entries = get_all_bibliography_data(doi_entries, driver)

    bib_entries = replace_citation_keys(bib_entries)

    (root, ext) = os.path.splitext(filename)
    bibtex_file = root + ".bib"

    with open(bibtex_file, 'w') as bib:
        for citation in bib_entries:
            print(citation, file=bib)

    print("Wrote generated BibTeX file as {}".format(bibtex_file))

def parse_file(filename):
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

    # Limit the length of citation keys
    if len(citation_key) > 20:
        error("Line {}: Citation key '{}' is over 20 characters".format(line_number, citation_key))

    if not doi_matcher.match(doi):
        error("Line {}: Invalid DOI '{}'".format(line_number, doi))

    return citation_key, doi

def get_all_bibliography_data(doi_entries, driver):
    """Takes a dict in the format {citation_key: doi_key}* and expands each doi key into its bibliography text"""

    print("Retrieving bibliography entries:")

    key_to_bibliography = {}

    for citation_key, doi in doi_entries.items():
        print("\t{} ({}) -> ".format(citation_key, doi), end="")
        bibliography_text = driver.get_entry(doi)
        print("Done.")

        key_to_bibliography[citation_key] = bibliography_text

    return key_to_bibliography


def replace_citation_keys(key_to_bibliography):
    """Single the bibtex entry comes with a default citation key, we need to replace
    this with the key specified in the file"""

    bib_items = []

    for citation_key in key_to_bibliography:
        bib_text = key_to_bibliography[citation_key]

        citation_key_match = bibtex_key_matcher.match(bib_text)

        if not citation_key_match:
            error("Ill formatted bibtex entry:\n{}".format(bib_text))

        old_key = citation_key_match.group(1)

        new_bib = bib_text.replace(old_key, citation_key)

        bib_items.append(new_bib)

    return bib_items

def error(msg):
    sys.exit(msg)
