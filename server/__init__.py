def register_extensions(app):
    """
    Register your flask extensions
    """
    from .extensions import db, admin, migrate, login, ckeditor
    from .auth.models import User


    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    admin.init_app(app)
    ckeditor.init_app(app)

    # Login user loader
    @login.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()
    

def register_blueprints(app):
    """
    Register your application blueprints
    """
    from server.pages import pages
    from server.auth import auth
    from server.blogs import blogs

    app.register_blueprint(pages)
    app.register_blueprint(auth)
    app.register_blueprint(blogs)


# ----------- Context Processors and Error Handlers ----------- #
def apply_themes(app):
    from flask import render_template
    from .utils import context

    ## Error Handling
    # Handle 404
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html', error=e), 404

    # Handle 500
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html', error=e), 500

    # Bad Gateway
    @app.errorhandler(502)
    def internal_server_error(e):
        return render_template('502.html', error=e), 502

    ## Jinja Function
    @app.context_processor
    def context_processor():
        return dict(
                format_date = context['format_date'],
                format_time = context['format_time']
            )
    

def create_app():
    """
    Create and configure flask application
    """
    from flask import Flask
    from dotenv import load_dotenv
    # Load environment variables
    load_dotenv()
    from .extensions import UPLOADS
    import os

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    # Create directories if not exists
    for dir in UPLOADS:
        if not os.path.exists(UPLOADS[dir]):
            os.makedirs(UPLOADS[dir])

    with app.app_context():
        register_extensions(app)
        apply_themes(app)
        register_blueprints(app)

        return app