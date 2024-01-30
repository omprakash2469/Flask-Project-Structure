from flask import redirect, request
from slugify import slugify
from wtforms.fields import FileField
from flask_admin.contrib.sqla import ModelView
from flask_admin import expose
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os

from .models import User
from ..extensions import UPLOADS

class UsersView(ModelView):
    column_searchable_list = ("name", "email")
    column_list = ("name", "email", "profile_image", "registration_date", "last_login")
    form_excluded_columns = ("registration_date", "last_login")

    form_overrides = {
        "profile_image": FileField
    }

    @expose("/create/", methods=['GET', 'POST'])
    def create_view(self, *args, **kwargs):
        # Override the create view
        self._template_args['form'] = self.create_form(self)
        return super(UsersView, self).create_view(*args, **kwargs)

    def on_model_change(self, form, model, is_created):
        # Override the on_model_change method to handle password encryption and save
        password = form.password.data
        image = form.profile_image.data

        if password:
            # Hash the password before saving it to the database
            model.password = User.get_password_hash(model)
            model.registration_date = datetime.now()
            model.last_login = datetime.now()

        if image:
            slug = slugify(form.name.data)
            model.upload_profile_image(image)
            
            # Configure Image
            image_name = secure_filename(slug + os.path.splitext(image.filename)[1])
            image_path = os.path.join(UPLOADS['user_profile'], image_name)
            model.profile_image = image_name
            
            # Upload image if not already exists
            if not os.path.exists(image_path):
                image.save(image_path)

        # Call the parent on_model_change to perform the default behavior
        return super(UsersView, self).on_model_change(form, model, is_created)