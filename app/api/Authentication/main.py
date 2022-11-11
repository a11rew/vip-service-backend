from fastapi import FastAPI
from ...db.models.models import UserLoginSchema, User
from .jwthandler import signJWT
from fastapi import FastAPI, Body


app = FastAPI()

users = [] ### NOTE This is what I used for the database of the user ----> It's just a dummy 


### SIGNUP
# @app.post('/user/signup', tags=['User'])
# def user_signup(user: User=Body(default=None)):
#     users.append(user)
#     return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True    
        return False 


### LOGIN
@app.post('/user/login', tags=['User'])
def user_login(user: UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            'error': 'invalid login details'
        }
