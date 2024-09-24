from flask import Flask

import os

app = Flask(__name__)
app.config["SECRECT_KEY"] = os.getenv("ons_dummy_secret_key")

from ons_dummy import routes
