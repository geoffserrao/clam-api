__version__ = "1.0"

from fastapi import FastAPI

app = FastAPI()

from . import main
