from flask import Flask
from flask_bootstrap import Bootstrap

#its the init file innit?
def create_app():
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    from . import views
    app.register_blueprint(views.main_blueprint)
    return app