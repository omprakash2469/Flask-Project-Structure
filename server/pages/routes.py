from flask import render_template, stream_template

from . import pages
from ..blogs.models import PostsCategories

@pages.route("/")
def home():
    return stream_template('index.html')

@pages.route("/blogs")
def blogs():
    return render_template('pages/blogs.html', categories=PostsCategories.query.all())

@pages.route("/about-us")
def about():
    return render_template('pages/about.html')

@pages.route("/contact-us")
def contact():
    return render_template('pages/contact.html')