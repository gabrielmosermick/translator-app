from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to a specific frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

import json
with open("translations.json", "r") as file:
    translations = json.load(file)

def to_jeringoza(text: str) -> str:
    vowels = "aeiouAEIOU"
    jeringoza_text = ""
    for char in text:
        jeringoza_text += char
        if char in vowels:
            if char.islower():
                jeringoza_text += "p" + char
            else:
                jeringoza_text += "P" + char.lower()
    return jeringoza_text

class TranslationRequest(BaseModel):
    text: str
    language: str

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    if request.text != "Hello. How are you?":
        raise HTTPException(status_code=400, detail="Invalid text. Only 'Hello. How are you?' is allowed.")
    
    translation = translations.get(request.language.lower())
    if not translation:
        raise HTTPException(status_code=400, detail="Unsupported language.")
    
    return {"translated_text": translation}

@app.post("/jeringoza")
async def translate_to_jeringoza(request: TranslationRequest):
    return {"translated_text": to_jeringoza(request.text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)