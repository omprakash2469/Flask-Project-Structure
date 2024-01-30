from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_ckeditor import CKEditor
import os


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
ckeditor = CKEditor()


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))
    
admin = Admin(name="DEMO", index_view=MyAdminView(), template_mode="bootstrap4")



# Base Upload directory
UPLOADS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads/")

# Upload sub-directories
UPLOADS = {
    "user_profile": os.path.join(UPLOADS_DIR, "profiles/")
}