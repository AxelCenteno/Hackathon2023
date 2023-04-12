from flask import Flask
app = Flask(__name__)

from .views import views

app.register_blueprint(views, url_prefix='/')