from datetime import datetime

from ..extensions import db


class PostsCategories(db.Model):
    __tablename__ = 'posts_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    posts = db.relationship("Posts", backref="category")
    date = db.Column(db.DateTime, default=datetime.now())

    
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    meta_description = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    thumbnail_image = db.Column(db.String(255), nullable=False)
    header_image = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("posts_categories.id"))
    content = db.Column(db.Text, nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime, default=datetime.now())