class ApplicationException(Exception):
    def __init__(self, message: str, status_code: int = 500, internal_code: str = "E000"):
        self.message = message
        self.status_code = status_code
        self.internal_code = internal_code

    def to_dict(self):
        return {
            "message": self.message,
            "code": self.internal_code,
            "status": self.status_code
        }