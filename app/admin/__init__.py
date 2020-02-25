from flask import redirect, url_for, request
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from app import db, admin_app
from app.auth.models import User
from app.blog.models import *


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("login", next=request.url))


admin_app.add_view(AdminModelView(User, db.session))
admin_app.add_view(AdminModelView(Post, db.session))
admin_app.add_view(AdminModelView(Category, db.session))
admin_app.add_view(AdminModelView(Tag, db.session))


from flask import Blueprint

admin_blueprint = Blueprint("custom_admin", __name__)

from app.admin import forms, models, views
