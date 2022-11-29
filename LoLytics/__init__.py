from flask import Flask, render_template
from LoLytics.settings import DevConfig
from LoLytics.overview import overview_bp
from LoLytics.player import player_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(overview_bp)
    app.register_blueprint(player_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
