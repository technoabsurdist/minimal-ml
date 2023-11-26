from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    source: str
    target: str

class TranscriptionRequest(BaseModel):
    url: str

class DetectLanguageRequest(BaseModel):
    text: str

class DetectAndTranslate(BaseModel):
    text: str
    target: str

