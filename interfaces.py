from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    source: str
    target: str

class TranscriptionRequest(BaseModel):
    url: str