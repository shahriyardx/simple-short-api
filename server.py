import asyncio

from hypercorn import Config
from hypercorn.asyncio import serve

from src.app import app
from src.utils.env import env

config = Config()
config.bind = f"{env.HOST}:{env.PORT}"
config.use_reloader = False

asyncio.run(serve(app, config))
