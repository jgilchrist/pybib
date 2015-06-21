import pprint
import sys

from collections import namedtuple

import termstyle
from termstyle import red, cyan, green, magenta

# Automatically disable output colors if the output is not a terminal
termstyle.auto()

# Stores each part of the citation
Parts = namedtuple('Parts', ['type', 'title', 'authors', 'date', 'container', 'extra', 'doi'])

# A formatter consists of a name, corresponding to the name of the type of
# citation which can be formatted, and a function which adds extra information
# to the Parts object
Formatter = namedtuple('Formatter', ['name', 'func'])

# The template controls the structure of the output from the tool when searching
template = '{parts.title}\n\t{parts.authors}{parts.extra} ({parts.date}) [{parts.type}], \n\t{parts.doi}'


def color_parts(parts):
    """Adds colors to each part of the citation"""
    return parts._replace(
        title=green(parts.title),
        doi=cyan(parts.doi)
    )

def get_common_parts(r):
    """Gets citation parts which are common to all types of citation"""

    def format_title(title):
        return title[0]

    def format_author_list(authors):
        author_list = []

        if not authors:
            return "Anonymous"

        for author in authors:
            given_name = author.get("given", "")
            family_name = author.get("family", "")

            if given_name:
                # Only include the first letter of the author's given name
                given_name = "{}.".format(given_name[0])

            full_name = " ".join([given_name, family_name])
            author_list.append(full_name)

        return ', '.join(author_list)

    def format_container(container_titles):
        return ', '.join(container_titles)

    def format_date(date):
        date_parts = date.get('date-parts')[0]
        year = date_parts[0]

        return year

    title = format_title(r.get('title'))
    author_list = format_author_list(r.get('author'))
    container = format_container(r.get('container-title'))
    date = format_date(r.get('issued'))
    doi = r.get('DOI')

    return Parts(type='Unknown', title=title, authors=author_list, container=container, date=date, extra='', doi=doi)


def format_book(r, parts):
    # pprint.pprint(r)
    # {book} pp. {pages}
    return ''

def format_book_chapter(r, parts):
    return ''

def format_component(r, parts):
    # pprint.pprint(r)
    return ''

def format_dataset(r, parts):
    # pprint.pprint(r)
    return ''

def format_dissertation(r, parts):
    # pprint.pprint(r)
    return ''

def format_journal(r, parts):
    # pprint.pprint(r)
    return ''

def format_journal_article(r, parts):
    # pprint.pprint(r)
    return ''

def format_monograph(r, parts):
    # pprint.pprint(r)
    return ''

def format_proceedings_article(r, parts):
    # pprint.pprint(r)
    return ''

def format_reference_entry(r, parts):
    # pprint.pprint(r)
    return ''

def format_report(r, parts):
    # pprint.pprint(r)
    return ''

def format_standard(r, parts):
    # pprint.pprint(r)
    return ''

def format_unknown(r, parts):
    print(red('Unknown type: "%s"' % r.get('type')), file=sys.stderr)
    return ''


formatters = {
    'book': Formatter('Book', format_book),
    'book-chapter': Formatter('Book Chapter', format_book_chapter),
    'component': Formatter('Component', format_component),
    'dataset': Formatter('Dataset', format_dataset),
    'dissertation': Formatter('Dissertation', format_dissertation),
    'journal': Formatter('Journal', format_journal),
    'journal-article': Formatter('Journal Article', format_journal_article),
    'monograph': Formatter('Monograph', format_monograph),
    'proceedings-article': Formatter('Proceedings Article', format_proceedings_article),
    'reference-entry': Formatter('Reference Entry', format_reference_entry),
    'report': Formatter('Report', format_report),
    'standard': Formatter('Standard', format_standard),
}

unknown_formatter = Formatter('Unknown', format_unknown)


def format(r):
    reference_type = r.get('type')

    formatter = formatters.get(reference_type) or unknown_formatter

    parts = get_common_parts(r)
    parts = parts._replace(type=formatter.name)

    extra = formatter.func(r, parts)
    parts = parts._replace(extra=extra)

    parts = color_parts(parts)

    return template.format(parts=parts)
