from flask_admin.contrib.sqla import ModelView
from flask_admin import expose
from wtforms.fields import FileField, TextAreaField
from flask_ckeditor import CKEditorField
from slugify import slugify
import datetime

from ..blogs.models import Posts, PostsCategories
from ..extensions import admin, db


# Create your admin views here
class PostsCategoriesView(ModelView):
    column_list = ("id", "category", "slug", "date")
    form_excluded_columns = ("slug", "date")

    
    @expose("/create/", methods=['GET', 'POST'])
    def create_view(self, *args, **kwargs):
        # Override the create view
        self._template_args['form'] = self.create_form(self)
        return super(PostsCategoriesView, self).create_view(*args, **kwargs)


    def on_model_change(self, form, model, is_created):
        # Override the on_model_change method to create slug and datetime stamp
        slug = slugify(form.category.data)
        model.slug = slug

        # Call the parent on_model_change to perform the default behavior
        return super(PostsCategoriesView, self).on_model_change(form, model, is_created)


class PostsView(ModelView):
    column_list = ("title", "desc", "header_image", "category_id", "author", "created_at")
    form_args = {
        'desc': {
            'label': 'Description'
        }
    }
    form_widget_args = {
        'desc': {
            'style': 'color: black'
        }
    }
    form_excluded_columns = ("slug", "created_at", "last_updated")
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']
    form_overrides = {
        "thumbnail_image": FileField,
        "header_image": FileField,
        "meta_description": TextAreaField,
        "content": CKEditorField,
    }


# Register your views here
admin.add_sub_category(name="Blogs", parent_name="Blogs")
admin.add_view(PostsCategoriesView(PostsCategories, db.session, url="categories", name="Categories", category="Blogs"))
admin.add_view(PostsView(Posts, db.session, name="Posts", category="Blogs"))
