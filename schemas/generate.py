from pydantic import BaseModel

class GenerateForm(BaseModel):
    prompt_text: str
    image_link: str