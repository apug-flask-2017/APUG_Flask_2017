import re

from flask import Flask

app = Flask('hello')
app_stuff = str(dir(app))

kwords = ["session", "request", "response", "error", "jinja", "temp", "func", "test", "app"]

m = re.findall('.*?,', app_stuff)

def mk(m, k):
    for x in m:
        print(x)
    for kw in k:
        print(f'{kw}')
        for x in m:
            if kw in x:
                print(f'    {x}')
mk(m, kwords)

