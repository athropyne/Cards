from pydantic import BaseModel


class TokenModel(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    refresh_token: str


class AccountAcceptedModel(BaseModel):
    result: bool
    error_msg: str | None


