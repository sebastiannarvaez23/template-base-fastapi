from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.exceptions import RequestValidationError

from core.exceptions.base_exception import ApplicationException
from starlette.exceptions import HTTPException as StarletteHTTPException


async def app_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )