from flask import render_template

from . import blogs


@blogs.route("/posts")
def all_posts():
    return render_template('blogs/all-posts.html')


@blogs.route("/post")
def detail_post():
    return render_template('blogs/blog-details.html')