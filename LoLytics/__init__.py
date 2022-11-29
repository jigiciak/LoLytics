from flask import Flask, render_template
from LoLytics.settings import DevConfig
from LoLytics.overview import overview


def create_app():
    app = Flask(__name__)

    app.register_blueprint(overview)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
