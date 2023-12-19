import logging
from urllib.parse import urlparse
import os
import json
import datetime as dt
import uvicorn
import os

# import fastapi service modules
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse

# import starlette service modules
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware import Middleware
from router import router

fastapi_app = FastAPI()
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
fastapi_app.include_router(router)


if __name__ == "__main__":
    reload = True
    uvicorn_config = {
        "host": '0.0.0.0',
        "port": 8000,
        "reload": reload,
        "workers": 1,
        "log_level": "info",
    }
    print(uvicorn_config)
    uvicorn.run("main:fastapi_app", **uvicorn_config)