from flask import Flask
import bookingly.db


app = Flask(__name__)


# Known Circular dependency, this is expected
import bookingly.views
