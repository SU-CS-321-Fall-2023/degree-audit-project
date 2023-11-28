from flask import Flask
import os

def create_app():
    rootPath = os.path.abspath(os.getcwd())
    app = Flask(
        __name__,
        root_path = rootPath,
        template_folder= rootPath + "/front-end/src/templates",
        static_folder= rootPath + "/front-end/src/static")
    app.config['SECRET_KEY'] = 'hai'

    #from .views import views
    #app.register_blueprint(views, url_prefix='/')
    
    return app