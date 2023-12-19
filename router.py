# FastAPI Imports
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, FileResponse
from fastapi.security import (
    HTTPBearer,
)
from fastapi.templating import Jinja2Templates
from fastapi import (
    Depends,
    APIRouter,
    Request,
    Body,
    File,
    UploadFile,
    HTTPException,
)

# Starlette Imports
from starlette import status

# General Imports
import os
from typing import List
from pathlib import Path
import traceback
import glob
import shutil
import json

router = APIRouter(
    prefix="/home", tags=["home"], responses={404: {"description": "Not found"}}
)

templates = Jinja2Templates(directory="templates")

# Create an instance of HTTPBearer, which will handle extraction of the JWT token from the "Authorization" header
bearer_scheme = HTTPBearer()

@router.get("/dineshprofile", response_class=HTMLResponse)
async def load_profile(request: Request):
    
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
        },
    )