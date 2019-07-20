# coding: utf8
import os
import time
import requests
import bs4
import base64
import json
from bs4 import BeautifulSoup
from termcolor import colored
import textwrap


def lookup(word):
    base_url = 'https://www.vocabulary.com/dictionary/{}'
    audio_url = 'https://audio.vocab.com/1.0/us/{}.mp3'
    html = requests.get(base_url.format(word))
    soup = BeautifulSoup(html.content, features="html.parser")
    result = {
        'word': word,
        'url': html.url,
        'query_time': time.time(),
        'long': None,
        'short': None,
        'masked_short': None,
        'masked_long': None,
        'colored_short': None,
        'colored_long': None,
        'raw_short': None,
        'raw_long': None,
        'has_audio': False,
        'audio_url': None,
        'audio_data': None,
    }

    try:
        long_p = soup.findAll('p', {'class': 'long'})[0]
        short_p = soup.findAll('p', {'class': 'short'})[0]
    except:
        return None

    def process(p):
        r = []
        for t in p.children:
            if isinstance(t, bs4.element.Tag):
                r.append((1, t.text))
            else:
                r.append((0, t))
        return r

    def assemble(p, f):
        return ''.join(map(f, p))

    result.update({
        'long': long_p.text,
        'short': short_p.text,
        'raw_short': process(short_p),
        'raw_long': process(long_p)
    })

    result.update({
        'masked_short': assemble(result['raw_short'], lambda t: t[1] if t[0] == 0 else '[...]'),
        'masked_long': assemble(result['raw_long'], lambda t: t[1] if t[0] == 0 else '[...]'),
        'colored_short': assemble(result['raw_short'], lambda t: t[1] if t[0] == 0 else colored(t[1], 'red')),
        'colored_long': assemble(result['raw_long'], lambda t: t[1] if t[0] == 0 else colored(t[1], 'red'))
    })

    try:
        audio_data = soup.findAll('a', {'class': 'audio'})[0].attrs['data-audio']
        audio_data = requests.get(audio_url.format(audio_data))
    except:
        return result

    result.update({
        'has_audio': True,
        'audio_url': audio_data.url,
        'audio_data_base64_ascii': base64.encodebytes(audio_data.content).decode('ascii')
    })

    return result


def formated_print(content, width=80):
    print(textwrap.fill(content, width=width))


def add_note(result):
    note = {
        "deckName": "GRE",
        "modelName": "vocabulary.com",
        "fields": {
            "word": result['word'],
            "short": result['short'],
            "long": result['long'],
            "masked_short": result['masked_short']
        },
        "tags": [],
    }

    if result['has_audio']:
        note['audio'] = {
            "url": result['audio_url'],
            "filename": "{}.mp3".format(result['word']),
            "fields": ["audio"]
        }

    data = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": note
        }
    }

    try:
        r = requests.post('http://localhost:8765', data=json.dumps(data))
        print(r.json())
    except:
        print('can not connect to server, not added')


if __name__ == "__main__":
    db_path = 'db.json'
    try:
        db = json.load(open(db_path, 'r'))
    except:
        db = {}
    try:
        while True:
            word = input("look up > ")
            result = lookup(word)
            if result is None:
                print("Not found")
            else:
                print(colored(result['word'], 'red'))

                if result['has_audio']:
                    print(colored(result['audio_url'], 'green'))

                print('-' * 80)
                formated_print(result['colored_short'])
                print('-' * 80)
                formated_print(result['colored_long'])
                print('-' * 80)
                add_note(result)
                db[word] = result
    except:
        print('exiting ... ', end='')
        json.dump(db, open(db_path, 'w'), sort_keys=True, indent=2)
        print('data saved to {}'.format(db_path))
