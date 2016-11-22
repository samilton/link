from app import app
from app import models


@app.route("/")
def index():
    return "Hello World"


@app.route("/alias/<name>")
def get_alias(name):
    aliases = models.Alias.query.first()
    return "Hello %s" % aliases.name
