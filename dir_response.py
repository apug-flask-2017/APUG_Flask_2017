import re

from flask import Flask

app = Flask('hello')
resp_stuff = str(dir(app.response_class()))

kwords = ["form", "get", "set", "content", "cookie", "resp", "stat", "cod", "app"]

m = re.findall('.*?,', resp_stuff)

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
