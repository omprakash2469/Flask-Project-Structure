from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from slugify import slugify
import os

from ..extensions import db
from ..extensions import UPLOADS

# Your auth models 
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(500), default="profile.png")
    registration_date = db.Column(db.DateTime)
    # posts = db.relationship("Posts", backref="users")
    last_login = db.Column(db.DateTime)

    def get_password_hash(self):
        """
        Returns the hash of the given password
        """
        return generate_password_hash(self.password)
    
    
    def upload_profile_image(self, image):
        """
        Upload the profile image of the user
        """
        # Image Upload Configuration
        slug = slugify(f"{self.id}_{self.name}")
        imageName = secure_filename(slug + os.path.splitext(image.filename)[1])
        imagePath = os.path.join(UPLOADS["user_profile"], imageName)
        
        if not os.path.exists(imagePath):
            image.save(imagePath)
