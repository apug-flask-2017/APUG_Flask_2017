# This file drives the Flask application

# If we leave the previous example running, the attempt to run this
# version will fail for trying to use the same port.

# When we stop the other process, this still fails because we forgot
# to import the views module.

# Then stop this process, and change the port number.  That will
# allow both processes to run at the same time.

from hwf import hwf
from hwf import views

hwf.run(port=5002)