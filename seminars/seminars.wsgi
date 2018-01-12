#!/usr/bin/python
import os
import sys
import logging
logging.basicConfig(stream=sys.stderr)

here = os.path.dirname(__file__)
activate_this = os.path.join(here, "venv/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

path = os.path.join(here, os.pardir)
if path not in sys.path:
    sys.path.append(path)

from seminars import app as application
