from quart import Quart
from quart_cors import cors

from .db import prisma
from .shorten import bp as shorten_blueprint

app = Quart(__name__)

app = cors(app, allow_origin="*", allow_headers="*", allow_methods="*")
app.register_blueprint(shorten_blueprint)


@app.before_serving
async def serve():
    await prisma.connect()
