# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.bot import scrape
from nlplogic.corenlp import get_phrases

app = FastAPI()

class Wiki(BaseModel):
    name: str


@app.post("wiki")
async def scrape_story(wiki: Wiki):
    result = scrape(name=wiki.name)
    payload = {"wikipage": result}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Hello NLP"}

@app.get("/wikiphrases/{name}")
async def wikiphrase(name: str):

    print(f"Passed in {name}")
    noun_phrases = get_phrases(name)
    return {"noun_pherases": noun_pherases}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')