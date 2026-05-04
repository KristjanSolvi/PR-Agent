import yaml
from flask import Flask, redirect, request, render_template_string

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"


@app.route("/login")
def login():
    next_url = request.args.get("next", "/")
    return redirect(next_url)


@app.route("/profile")
def profile():
    name = request.args.get("name", "guest")
    template = "<h1>Hello " + name + "</h1>"
    return render_template_string(template)


@app.route("/import", methods=["POST"])
def import_settings():
    raw = request.data
    settings = yaml.load(raw, Loader=yaml.Loader)
    return {"loaded": settings}


@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


@app.route("/set_session")
def set_session():
    response = app.make_response("ok")
    response.set_cookie("session", request.args.get("sid", ""))
    return response
