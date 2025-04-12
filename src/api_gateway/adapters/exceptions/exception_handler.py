from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from features.user.person.domain.exceptions.person_exceptions import (
    PersonAlreadyExistsException,
    PhoneAlreadyExistsException
)

async def person_exceptions_handler(request: Request, exc: Exception):
    if isinstance(exc, PersonAlreadyExistsException) or isinstance(exc, PhoneAlreadyExistsException):
        return JSONResponse(
            status_code=HTTP_409_CONFLICT,
            content={
                "error_code": getattr(exc, "internal_code", "UNKNOWN"),
                "detail": str(exc)
            }
        )

    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": "Unexpected error"}
    )