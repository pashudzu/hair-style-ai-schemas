from pydantic import BaseModel, AnyUrl, UUID4

class GenerateForm(BaseModel):
    prompt_text: str
    image_link: AnyUrl
    user_id: UUID4