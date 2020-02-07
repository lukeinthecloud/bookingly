from bookingly.server import app, api_route_blueprint
from .user import user_routes


@app.route('/')
def index():
    return 'Welcome to the Bookingly API please read the docs to see what you can access!'


app.register_blueprint(api_route_blueprint, url_prefix='/api/v1')
