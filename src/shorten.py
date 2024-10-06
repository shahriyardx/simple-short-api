from prisma.errors import UniqueViolationError
from quart import Blueprint, Response, abort, redirect, request

from .db import prisma
from .utils.text import generate_random_string

bp = Blueprint("shorten", __name__)


@bp.route("/shorten", methods=["POST"])
async def shorten():
    body = await request.json
    text = body.get("text")
    url = body.get("url")

    if not text:
        text = generate_random_string(4)

    try:
        data = await prisma.url.create(
            data={"text": text, "destination": url},
        )
    except UniqueViolationError:
        return {
            "success": False,
            "error": "Duplicate URL detected",
        }

    return {
        "success": True,
        "url": data.destination,
        "text": text,
    }


@bp.route("/<string:text>")
async def view(text):
    data = await prisma.url.find_first(where={"text": text})
    if not data:
        abort(Response("Not found", 404))

    return redirect(data.destination, 301)
