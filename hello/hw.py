# Hello World in a single file

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

app.run()

# after demonstrating basic operation
#   change the HW message
#
#   show that refresh of browser does not change the message
#
#   stop the execution and restart
#
#   show that refresh of browser now shows the changed message
#
# NEXT: Break up the single file into "package" structure.

