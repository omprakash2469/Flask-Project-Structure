import os

# Application configuration
DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Flask Admin Configurations
FLASK_ADMIN_SWATCH = 'cerulean'
FLASK_ADMIN_FLUID_LAYOUT = True