

from . import hwd


@hwd.route('/')
def index():
    return 'Hello, World! via hw_dirs'