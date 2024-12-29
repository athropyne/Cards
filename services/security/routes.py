from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from faststream.redis.fastapi import RedisRouter

from core.config import settings
from services.security.dto import TokenModel, AccountAcceptedModel

router = RedisRouter(settings.BROKER_URI,prefix="/security")

@router.subscriber("account_accepted")
async def account_accepted_handler(
        model: AccountAcceptedModel
):
    return model




@router.post("/",
             response_model=TokenModel)
async def auth(
        model: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
):
    response = router.broker.request()

