from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class ServerCreate(BaseModel):
    name: str
    host: str
    username: str
    password: str
