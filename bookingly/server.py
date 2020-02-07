from flask import Flask, Blueprint

base_path = '/api/v1'

app = Flask(__name__)

api_route_blueprint = Blueprint('api_route_blueprint', __name__)
