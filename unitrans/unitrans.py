import os
import json

charmap = {}

UNKNOWN = '[?]'  # Unknown character, default value


def load(path=None, unknown=None):
    if not path:
        base = os.path.dirname(__file__)
        path = os.path.join(base, 'data', 'map.json')
    with open(path) as data_file:
        for k, v in json.load(data_file).items():
            charmap[int(k)] = v
    # Unknown character
    charmap['?'] = unknown or UNKNOWN


def install(path=None, unknown=None):
    if not charmap:
        load(path=path, unknown=unknown)


def transliterate(text):
    result = []
    unknown = charmap['?']
    for x in text:
        s = charmap.get(ord(x), unknown)
        result.append(s)
    return ''.join(result)


if __name__ == '__main__':
    install()

    # print(json.dumps(charmap, indent=2))

    print("Мама мыла раму!")
    print(transliterate("Мама мыла раму!"))

    print("Пошёл ежик за йогуртом и попал в цивилизацию!")
    print(transliterate("Пошёл ежик за йогуртом и попал в цивилизацию!"))
