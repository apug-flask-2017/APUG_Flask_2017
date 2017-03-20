

from flask import render_template
from flask import request
from . import hwf



@hwf.route('/')
def index():
    return render_template('enter_name.html')

@hwf.route('/new_name', methods=['GET', 'POST'])
def gotta_name():
    show_stuff()
    return render_template("welcome.html", name=request.form['name'])

def show_stuff():
    print('\nForm Values:')
    for x in request.form:
        print(f'    {x}: {request.form[x]}')
