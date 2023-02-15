from flask import Flask
from flask import redirect
from flask_cors import CORS

from config import config

# Routes
from routes import PasswordRoutes

app = Flask(__name__)
CORS(app, resources = {"*": {'origins': 'http://localhost:5000'}})


@app.route('/')
def index():
    return redirect('/api/passwords')


def page_not_found(error):
    return "<h1>Error: page not found</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(PasswordRoutes.main, url_prefix = '/api/passwords')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(port = 5000)
