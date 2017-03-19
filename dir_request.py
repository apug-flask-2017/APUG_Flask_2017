import re

from flask import Flask

app = Flask('hello')
req_stuff = str(dir(app.request_class))

kwords = ["form", "url", "view", "error", "json", "head", "data", "cod", "app"]

m = re.findall('.*?,', req_stuff)

def mk(m, k):
    for x in m:
        print(x)
    for kw in k:
        print(f'{kw}')
        for x in m:
            if kw in x:
                print(f'    {x}')
    return

mk(m, kwords)
