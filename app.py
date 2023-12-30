from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ResponseBody(BaseModel):
    # Update class with art data.
    name: str = None
    title: str = None
    

@app.get('/endpoint')
def generate_art():


    response_body = ResponseBody()
    # Insert relevant art data into initialized response body.
    return response_body