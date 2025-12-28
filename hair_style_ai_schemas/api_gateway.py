from pydantic import BaseModel
from typing import Optional, Any, Dict

class StorageRequest(BaseModel):
    status: int
    text: Optional[str] = None
    json: Optional[Dict[str, Any]] = None
    headers: Dict[str, str]