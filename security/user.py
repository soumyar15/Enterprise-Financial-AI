from pydantic import BaseModel


class User(BaseModel):

    username: str

    role: str

    email: str