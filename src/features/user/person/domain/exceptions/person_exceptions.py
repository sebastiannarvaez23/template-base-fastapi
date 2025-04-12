from enum import Enum

from core.exceptions.base_exception import ApplicationException


class PersonErrorCode(str, Enum):
    EMAIL_ALREADY_EXISTS = "020001"
    PHONE_ALREADY_EXISTS = "020002"
    INVALID_PHONE_NUMBER = "020003"

class PersonAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.message = f"A person with the email '{email}' already exists."
        self.internal_code = PersonErrorCode.EMAIL_ALREADY_EXISTS
        super().__init__(self.message)


class PhoneAlreadyExistsException(Exception):
    def __init__(self, phone: str):
        self.message = f"A person with the phone number '{phone}' already exists."
        self.internal_code = PersonErrorCode.PHONE_ALREADY_EXISTS
        super().__init__(self.message)


class InvalidPhoneNumberException(Exception):
    def __init__(self):
        self.message = "The phone number provided is invalid."
        self.internal_code = PersonErrorCode.INVALID_PHONE_NUMBER
        super().__init__(self.message)