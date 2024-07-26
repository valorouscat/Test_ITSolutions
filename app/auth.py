from fastapi import  Request, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timezone, timedelta
import logging

from config import Config, allowed_hosts


# logging
logger = logging.getLogger(__name__)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# generating token for user
def create_jwt_token(data: dict):
    logger.info(f"Creating JWT token for user: {data['sub']}")
    return jwt.encode(data, Config.SECRET_KEY, algorithm=Config.ALGORITHM)

# generating token for user from db
@router.post("/login")
async def login(request: Request): 
    logger.info(f"Login request from: {request.client.host}")
    return {"access_token": create_jwt_token({"sub": request.client.host, "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=28_800)}), "token_type": "bearer"}

# checking if token is valid
async def auth_check(token: str = Depends(oauth2_scheme)):
    try:
        logger.info(f"Checking if token is valid: {token}")
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        host = payload.get("sub")
        if host in allowed_hosts:
            logger.info(f"Host {host} is allowed")
            return True
        logger.info(f"Host {host} is not allowed")
        raise HTTPException(status_code=401, detail="Access denied", headers={"WWW-Authenticate": "Bearer"})
    except jwt.ExpiredSignatureError:
        logger.info("Token has expired")
        raise HTTPException(status_code=401, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except jwt.InvalidTokenError:
        logger.info("Invalid token")
        raise HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})