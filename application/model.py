from pydantic import BaseModel, EmailStr, Field


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Some title about animals",
                "content": "Some content about animals",
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    pasword: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Bek",
                "email": "help@bekrace.com",
                "password": "123",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    pasword: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email": "help@bekrace.com",
                "password": "123",
            }
        }
