import atoma
import requests
from datetime import datetime
from secrets import TOKEN, CHATID


url = 'https://github.com/python/cpython/commits.atom'
response = requests.get(url)
feed = atoma.parse_atom_bytes(response.content)

updated = str(feed.updated)

with open('updated.txt') as f:
    line = f.readline()

if (line != updated):
    for entry in feed.entries:
        if str(entry.updated) != updated:
            link = entry.links[0].href
            # text = entry.content.value + ' ' + link
            text = link
            requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=html&text=%s' % (TOKEN, CHATID, text))
            with open('updated.txt', 'w') as f:
                fp.write(updated)
        else:
            break
