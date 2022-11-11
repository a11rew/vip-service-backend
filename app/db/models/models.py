from pydantic import BaseModel, Field, EmailStr


# class User(BaseModel):
#     fullname: str = Field(default=None)
#     email: EmailStr = Field(default=None)
#     password: str = Field(default=None)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "Uchechukwu Anachuna",
#                 "email": "uche.example@gmail.com",
#                 "password": "string"
#             }
#         }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "123"
            }
        }