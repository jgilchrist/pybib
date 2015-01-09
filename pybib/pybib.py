import re
import os
import sys
import requests

# Matches a valid DOI
doi_matcher = re.compile('(10\.\d{4}[\d\:\.\-\/a-z]+)')

# Matches a [citation_key DOI] pair
key_file_matcher = re.compile('(\w+)\s+(10\.\d{4}[\d\:\.\-\/a-z]+)')

# Matches the beginning of a BibTeX entry
bibtex_key_matcher = re.compile('@\w+{(\w+),')


def convert_file(filename, driver):
    """Convert a file in the format [citation_key doi_key]* into a valid bibtex file"""

    citation_key_to_doi = parse_file(filename)

    citation_key_to_bib = get_all_bibliography_data(citation_key_to_doi, driver)

    bibtex_lines = replace_citation_keys(citation_key_to_bib)

    (root, ext) = os.path.splitext(filename)
    bibtex_file = root + ".bib"

    with open(bibtex_file, 'w') as bib:
        for citation in bibtex_lines:
            print(citation, file=bib)

    print("Wrote generated BibTeX file as {}".format(bibtex_file))

def parse_file(filename):
    """Parses a file in the format [citation_key doi_key]* into a dictionary {citation_key: doi_key}*"""

    citation_key_to_doi = {}

    f = open(filename)
    lines = f.readlines()
    f.close()

    for line_number, line in enumerate(lines, start=1):

        parsed_line = parse_line(line_number, line)

        if parsed_line is None:
            # Line was blank, or a comment
            continue

        citation_key, doi = parsed_line

        # Don't allow duplicate citation keys
        if citation_key in citation_key_to_doi:
            sys.exit("Duplicate citation key: {} on line number {}".format(citation_key, line_number))

        citation_key_to_doi[citation_key] = doi

    print("Found {} citations in {}".format(len(citation_key_to_doi), filename))

    return citation_key_to_doi

def parse_line(line_number, line):
    """Parses a single line, of the format [citation_key DOI]"""

    if line.isspace():
        return None

    if line.startswith("#"):
        # Found a comment
        return None

    parsed_line = key_file_matcher.match(line)

    if not parsed_line:
        sys.exit("Invalid line ({}) in file: {}".format(line_number, line.strip()))

    citation_key, doi = parsed_line.group(1, 2)

    # Limit the length of citation keys
    if len(citation_key) > 20:
        sys.exit("Citation key '{}' is over 20 characters".format(citation_key))

    if not doi_matcher.match(doi):
        sys.exit("Invalid doi key.")

    return citation_key, doi

def get_all_bibliography_data(citation_key_to_doi, driver):
    """Takes a dict in the format {citation_key: doi_key}* and expands each doi key into its bibliography text"""

    print("Retrieving bibliography data... ", end="")

    key_to_bibliography = {}

    for citation_key, doi in citation_key_to_doi.items():
        bibliography_text = driver.get_entry(doi)

        key_to_bibliography[citation_key] = bibliography_text

    print("Done")

    return key_to_bibliography


def replace_citation_keys(key_to_bibliography):
    """Single the bibtex entry comes with a default citation key, we need to replace
    this with the key specified in the file"""

    bib_items = []

    for citation_key in key_to_bibliography:
        bib_text = key_to_bibliography[citation_key]

        citation_key_match = bibtex_key_matcher.match(bib_text)

        if not citation_key_match:
            sys.exit("Ill formatted bibtex entry:\n{}".format(bib_text))

        old_key = citation_key_match.group(1)

        new_bib = bib_text.replace(old_key, citation_key)

        bib_items.append(new_bib)

    return bib_items
