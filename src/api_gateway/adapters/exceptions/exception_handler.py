from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND

from features.user.person.domain.exceptions.person_exceptions import (
    PersonAlreadyExistsException,
    PhoneAlreadyExistsException,
    PersonNotFoundException
)


async def person_exceptions_handler(request: Request, exc: Exception):
    if isinstance(exc, PersonAlreadyExistsException) or isinstance(exc, PhoneAlreadyExistsException):
        return JSONResponse(
            status_code=HTTP_409_CONFLICT,
            content={
                "internal_code": getattr(exc, "internal_code", "UNKNOWN"),
                "detail": str(exc)
            }
        )
    
    if isinstance(exc, PersonNotFoundException) or isinstance(exc, PersonNotFoundException):
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={
                "internal_code": getattr(exc, "internal_code", "UNKNOWN"),
                "detail": str(exc)
            }
        )

    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": "Unexpected error"}
    )