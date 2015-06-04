import requests
import json

GET_URL = "http://dx.doi.org/{}"
SEARCH_URL = "http://api.crossref.org/works"

def handle_status_code(r):
    if r.status_code == 200:
        return
    elif r.status_code == 404:
        exit('Unknown')
    else:
        sys.exit("Unhandled http response code: {}".format(r.status_code))

def search(query):
    payload = {'query': query}

    r = requests.get(SEARCH_URL, params=payload)
    r.encoding = "utf-8"

    handle_status_code(r)

    results = r.json()
    results = results["message"]["items"]
    return results

def get_bibtex(doi):
    url = GET_URL.format(doi)
    headers = {'Accept': 'application/x-bibtex; charset=utf-8'}

    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"

    handle_status_code(r)

    entry = r.text.strip()
    return entry
