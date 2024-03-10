import time
import atoma
import requests
from datetime import datetime
from secret import TOKEN, CHATID

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
           'Accept':'application/atom+xml'}
url = 'https://github.com/python/cpython/commits.atom'
response = requests.get(url, headers=headers)
feed = atoma.parse_atom_bytes(response.content)

updated = str(feed.updated)
messages = []

with open('updated.txt') as f:
    last = str(f.readline())

if (last != updated):
    for entry in feed.entries:
        if str(entry.updated) != last:
            link = entry.links[0].href
            messages.append(link)
        else:
            break

    messages.reverse()
    for message in messages:
        requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&parse_mode=html&text=%s' % (TOKEN, CHATID, message))
        time.sleep(2)

    with open('updated.txt', 'w') as f:
        f.write(updated)
