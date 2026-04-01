from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .schema import AnetApiResponse


class AuthorizeNetError(Exception):
    """Raised when the Authorize.Net API returns an error response.

    Attributes:
        response: The parsed response object containing error details.
        code: The first error code from the messages (e.g., "E00035").
        message: The first error message text.
    """

    def __init__(self, response: "AnetApiResponse") -> None:
        self.response = response
        self.code: str = ""
        self.message: str = ""
        if response.messages and response.messages.message:
            first = response.messages.message[0]
            self.code = first.code
            self.message = first.text
        super().__init__(f"[{self.code}] {self.message}")
