from app import db
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.main import main_blueprint
from app.main.models import Model
from app.main.forms import Form


@main_blueprint.route("/", methods=["GET"])
def index():
    return render_template("base.html", context={})


@main_blueprint.route("/explore", methods=["GET"])
def explore():
    return render_template("base.html", context={})
