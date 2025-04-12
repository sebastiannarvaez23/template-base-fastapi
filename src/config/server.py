import uvicorn
import os

from fastapi import FastAPI


class Server:
    def __init__(self, app: FastAPI):
        self.app = app
        self.host = os.getenv("APP_HOST", "0.0.0.0")
        self.port = int(os.getenv("APP_PORT", 8000))

    def raise_server(self):
        uvicorn.run(self.app, host=self.host, port=self.port)