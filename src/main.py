import asyncio

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from dotenv import load_dotenv
from starlette.exceptions import HTTPException as StarletteHTTPException

from api_gateway.adapters.http.app_routes import init_routes
from api_gateway.adapters.exceptions.exception_handler import person_exceptions_handler
from config.database import DatabaseConfig
from config.server import Server
from config.session import init_db
from core.exceptions.base_exception import ApplicationException
from utils.handlers.exception_handler import (
    app_exception_handler,
    validation_exception_handler,
    http_exception_handler
)
from features.user.person.domain.exceptions.person_exceptions import (
    PersonAlreadyExistsException,
    PhoneAlreadyExistsException,
    PersonNotFoundException
)


load_dotenv()

app = FastAPI(
    title="Template base FastAPI",
    description="Template base for creating backends in fastapi.",
    version="1.0.0" 
)
init_routes(app)

# REFACTORIZAR PARA QUE HAYA UNA FUNCION QUE EJECUTE TODOS LOS HANDLERS
app.add_exception_handler(ApplicationException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(PersonAlreadyExistsException, person_exceptions_handler)
app.add_exception_handler(PhoneAlreadyExistsException, person_exceptions_handler)
app.add_exception_handler(PersonNotFoundException, person_exceptions_handler)
# ----

@app.on_event("startup")
async def startup():
    db = DatabaseConfig()
    await db.authenticate()
    await init_db()

if __name__ == "__main__":
    server = Server(app)
    server.raise_server()
