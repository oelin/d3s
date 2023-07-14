"""Daily dose of data science."""


import random
import textwrap
from urllib.parse import quote as urlencode
import requests
import pyquery
from titlecase import titlecase
from d3s.topics import topics


def main():
    while True:
        topic = random.choice(topics)

        response = requests.get(f'https://api.wikimedia.org/core/v1/wikipedia/en/page/{urlencode(topic)}/html').text
        document = pyquery.PyQuery(response)
        prologue = document.find('section[data-mw-section-id="0"] > p')

        if not prologue:
            continue

        prologue = prologue.text()
        prologue = prologue.replace('\n', '')

        print(titlecase(topic))
        print('-'*len(topic))
        print(textwrap.fill(prologue, width=70))

        break
