from pydantic import BaseModel, field_validator, Field

class UploadFileForm(BaseModel):
    file_name: str = Field(...)
    bucket_name: str = Field(...)

    @field_validator("file_name")
    def file_name_ending(cls, v) -> str:
        if not v.endswith((".jpg", ".jpeg", ".png")):
            raise ValueError("File must be an image")
        return v
    
class GetFileForm(BaseModel):
    bucket_name: str = Field(...)
    file_key: str = Field(...)

class ListFilesForm(BaseModel):
    bucket_name: str = Field(...)

class CreatePresignedUrlForm(BaseModel):
    operation: str = Field(...)
    bucket_name: str = Field(...)
    file_key: str = Field(...)
    expires_in: int = Field(...)