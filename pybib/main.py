import argparse
import pybib
import termstyle
import sys

def search_cmd(args):
    query = " ".join(args.query)
    results = pybib.search(query)

    # Only get the first 10 results
    results = results[:10]

    if args.get:
        idx = args.get[0]
        result = results[idx]
        doi = result["DOI"]
        entry = pybib.get_bibtex(doi)
        print(entry)
        return

    for i, result in enumerate(results):
        formatted_result = pybib.format_entry(result)
        print('{}. {}'.format(i, formatted_result))


def get_cmd(args):
    entry = pybib.get_bibtex(args.DOI)

    termstyle.disable()
    print(entry)
    termstyle.enable()


def main():
    parser = argparse.ArgumentParser(description='Retrieve BibTeX information for Digital Object Identifiers (DOIs)')
    parser.add_argument('--version', action='version', version=pybib.__version__)

    subparsers = parser.add_subparsers()

    get_parser = subparsers.add_parser('get', help='Retrieve an entry for a DOI')
    get_parser.add_argument('DOI', type=str, help='The DOI to get')
    get_parser.set_defaults(cmd=get_cmd)

    search_parser = subparsers.add_parser('search', help='Search for the DOI of a resource')
    search_parser.add_argument('query', nargs='+', help='The query string')
    search_parser.add_argument('-g', '--get', nargs=1, type=int, help='The index of the bibliography information to get')
    search_parser.set_defaults(cmd=search_cmd)

    args = parser.parse_args()

    if not hasattr(args, 'cmd'):
        parser.print_help()
        sys.exit()

    args.cmd(args)