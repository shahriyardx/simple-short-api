import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Env:
    PORT: str = os.getenv("PORT", "5000")
    HOST: str = os.getenv("HOST", "0.0.0.0")


env = Env()
