# The function of this file is to check whether the request is authorized or not [verification of the protected route]

## NOTE I add this because for a user/company to use our api they have to be authenticated with their TOKEN like you said, so I created this to make some of the api LOGIN REQUIRED.

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwthandler import decodeJWT

class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request):
        credentials : HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request) ### NOTE here I am creating a variable named <credentials> from whatever <type> is gotten from HTTPAuthorizationCredentials
        if credentials:
            if not credentials.schema == 'Bearer':
                raise HTTPException(status_code=403, detail='Invalid or Expired Token')
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid or Expired Token')

    def verify_jwt(self, jwt_token: str): ## NOTE this is to check if the token is correct
        isValidToken : bool = False ## NOTE I am creating a variable called <isValidToken> from type <bool>
        payload = decodeJWT(jwt_token)
        if payload:
            isValidToken = True
        return isValidToken