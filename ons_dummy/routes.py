from flask.views import MethodView
from flask import render_template
from ons_dummy import app

import requests
import os

base_url = "https://api.github.com"

class HomeView(MethodView):
    def get(self):
        headers = {
            "Authorization": f"token {os.getenv("GITHUB_ACCESS_TOKEN")}"
        }
        user = requests.get(f"{base_url}/user", headers=headers).json()
        
        return render_template("home.html", user=user)


home_view = HomeView.as_view("home_view")

app.add_url_rule("/", view_func=HomeView.as_view("home_view"), methods=["GET"])

