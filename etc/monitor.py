"""
A webserver that waits for a GitHub webhook and updates relevant repositories.
"""

from flask import Flask
app = Flask(__name__)

@app.route("/update")
def update():

    # Update the repository.
    

    return "OK"