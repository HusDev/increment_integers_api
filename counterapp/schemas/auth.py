from ninja import Schema

class UserIn(Schema):
    id: int
    username: str
    first_name: str
    email: str
    
class UserCreateIn(Schema):
    username: str
    password: str
    email: str

class UserAuthDataIn(Schema):
    username: str
    password: str

class UserSchemaout(Schema):
    user: UserIn

class AuthSchemaOut(Schema):
    access: str
    user: UserIn