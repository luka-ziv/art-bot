from fastapi import FastAPI
from pydantic import BaseModel
import src.process as process    # Referenced from working dir (assigned locally by venv)

app = FastAPI()

class ImageResponse(BaseModel):
    b64image: str = None

class PromptResponse(BaseModel):
    children: list = None
    

@app.get('/image')
def generate_image_request(prompt: str):
    image_b64 = process.generate_image(prompt)
    response = ImageResponse()
    response.b64image = image_b64
    return response


@app.get('/prompts')
def generate_prompts_request(mother: str, num_children: int):
    children = process.generate_prompts(mother, num_children)
    response = PromptResponse()
    response.children = children
    return response