"""Daily dose of data science."""


import random
import textwrap
from urllib.parse import quote as urlencode
import requests
import pyquery
import colorama
from titlecase import titlecase
from d3s.topics import topics


def main() -> None:
    # Pick a random topic.

    while True:

        topic = random.choice(topics)

        # Get the corresponding Wikipedia page.

        response = requests.get(f'https://en.wikipedia.org/w/api.php?format=json&origin=*&action=query&prop=extracts&explaintext=false&exintro&titles={urlencode(topic)}').json()

        # Get the extract.

        query = response.get('query')
        if not query: continue

        pages = query.get('pages')
        if not pages: continue

        page = next(iter(pages.values()))
        if not page: continue

        extract = page.get('extract')
        if not extract: continue

        break

    print()
    print(colorama.Fore.WHITE + colorama.Style.BRIGHT + titlecase(topic))
    print(colorama.Fore.WHITE + colorama.Style.NORMAL + '-'*len(topic))
    print(colorama.Fore.WHITE + colorama.Style.NORMAL + textwrap.fill(extract, width=70))
    print()
