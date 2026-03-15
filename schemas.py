from pydantic import BaseModel, FilePath, EmailStr

class DomainRequest(BaseModel):
    domain: str
    credentials_file: FilePath
    email: EmailStr