from pathlib import Path

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from supabase import Client

from chronosphere.db import get_supabase_client
from chronosphere.db.crud import create_user
from chronosphere.schema import UserCreate
from chronosphere.templates import filters

app = FastAPI()

static_dir = Path(__file__).parent / "static"
static = StaticFiles(directory=static_dir)
app.mount("/static", static, name="static")


templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=templates_dir)
templates.env.filters.update(filters())


@app.get("/")
def read_root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("pages/index.html", {"request": request})


@app.get("/register")
def register(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("pages/register.html", {"request": request})
