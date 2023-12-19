import uvicorn
import os

reload = False
uvicorn_config = {
    "host": 'localhost',
    "port": 9810,
    "reload": reload,
    "workers": 1,
    "log_level": "info",
}
print(uvicorn_config)
uvicorn.run("main:fastapi_app", **uvicorn_config)