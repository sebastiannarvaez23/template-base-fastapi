from fastapi.responses import JSONResponse
from fastapi.requests import Request
from core.exceptions.base_exception import ApplicationException


async def application_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "message": exc.message,
                "code": exc.internal_code
            }
        }
    )