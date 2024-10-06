from quart import Blueprint, request, abort, Response
from .db import prisma
from .utils import generate_random_string
bp = Blueprint("psn", __name__, url_prefix="/")


@bp.route("/shorten", methods=["POST"])
async def shorten():
    body = await request.json
    text = body.get("text")
    url = body.get("url")

    if not text:
        text = generate_random_string(4)

    data = await prisma.url.create(
        data={"text": text, "destination": url},
    )

    return data

@bp.route("/<string:text>")
async def view(text):
    data = await prisma.url.findFirst(where={"text": text})
    if not data:
        abort(Response("Not found", 404))