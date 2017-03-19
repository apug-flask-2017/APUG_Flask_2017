

from . import hwd


@hwd.route('/')
def index():
    return 'Hello, World! via hw_dirs'

'''
#from flask import session
    #session['basic value'] = 'something'
@hwd.route('/<name>')
def hello_name(name):
    for x in session:
        print(f'session["{x}"] = {session[x]}')
    return f'Hello, {name}!'
'''
