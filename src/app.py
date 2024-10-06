from quart import Quart
from quart_cors import cors

from .shorten import bp as shorten_blueprint

app = cors(Quart(__name__), allow_origin="*", allow_headers="*", allow_methods="*")

app.register_blueprint(shorten_blueprint)
