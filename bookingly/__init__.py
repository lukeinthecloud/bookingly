from flask import Flask

app = Flask(__name__)

# Known Circular dependency, this is expected
import bookingly.views
