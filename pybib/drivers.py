import sys
import requests

class Driver:

    def get_entry(self, doi):
        (url, headers) = self.get_api_url(doi)

        r = requests.get(url, headers=headers)
        r.encoding = "utf-8"

        if r.status_code == 200:
            pass
        elif r.status_code == 404:
            sys.exit("Unknown doi key.")
        else:
            sys.exit("Unhandled http response code: {}".format(r.status_code))

        entry = r.text.strip()

        return entry


class DXDoi(Driver):
    # This website allows information about a paper to be retrieved by accessing
    # http://dx.doi.org/DOI

    def __init__(self):
        self.url = "http://dx.doi.org/"

    def get_api_url(self, doi):
        url = self.url + doi
        headers = {'Accept': 'application/x-bibtex; charset=utf-8'}

        return (url, headers)

class CrossRef(Driver):

    def __init__():
        pass

    def get_api_url(self, doi):
        raise NotImplementedError('Cannot currently use CrossRef to retrieve entries')
