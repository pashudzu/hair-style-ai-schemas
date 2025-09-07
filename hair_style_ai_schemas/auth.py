import re
from pydantic import BaseModel, EmailStr, Field, field_validator

class RegistrationForm(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    @field_validator("username")
    def username_complexity(cls, v) -> str:
        if not re.fullmatch(r"[a-zA-Z0-9_-.]{6,25}", v):
            raise ValueError("Username must contain only Latin letters, digits and allowed symbols(_-.). Minimum size is 6 and maximum is 25")
        return v

    @field_validator("password")
    def password_complexity(cls, v) -> str:
        if not re.fullmatch(r"[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};:'\",.<>/?|`~]{6,64}", v):
            raise ValueError("Password must contain only Latin letters, digits and allowed symbols(!@#$%^&* etc). Minimum size is 6 and maximum is 64.")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain at least one digit.")
        return v

class LoginForm(BaseModel):
    email_or_username: str = Field(..., pattern=r"^[a-zA-Z0-9_-. +-@]+$", max_length=254)
    password: str = Field(...)