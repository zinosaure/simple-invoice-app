import os
import time

from fastapi import status, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from jinja2 import Environment, FileSystemLoader


# FastAPI
app = FastAPI(title=os.getenv("WEBAPP_TITLE", "FastAPI"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory="public/"), name="public")

# Jinja2 Env
env = Environment(loader=FileSystemLoader(["app/html/"]))


@app.get("/{_:path}")
def home(request: Request):
    return HTMLResponse(
        status_code=status.HTTP_200_OK,
        content=env.get_template("index.html").render({"timestamp": time.time()}),
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
        },
    )
