from pydantic import BaseModel, EmailStr, Field

class RegistrationForm(BaseModel):
    username: str = Field(..., min_length=6, max_length=25)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6, max_length=128)

class LoginForm(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)