def convert_lower(inp_list):
    return list(map(lambda word: word.lower(), inp_list))

from pathlib import Path
import json

json_location = Path(__file__).absolute().parent
unsafe_words_json = json_location / 'unsafe_words.json'
unsafe_words = open(unsafe_words_json)
data = json.load(unsafe_words)


slurs_nsfw = convert_lower(data['slurs_and_nsfw'])
drugs = convert_lower(data['drugs'])
religions = convert_lower(data['religions'])
races = convert_lower(data['races'])

def is_safe(word):
    lower = word.lower()
    if lower in slurs_nsfw or lower in drugs or lower in religions or lower in races:
        return False
    else:
        return True