from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import googletrans

app = FastAPI()

class TextModel(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# @app.get("/translate/{msg}")
# async def translateMessage(msg: str):
#     translator = googletrans.Translator()
#
#     outStr = translator.translate(msg, dest='en', src='auto')
#     # print(f'{a=} {b=} {len(a)=}")
#     result = {
#         "original msg": msg,
#         "translate msg": outStr.text
#     }
#     return result
#     # return {"result": f"{outStr.text}"}

# @app.get("/sentiment/{text}")
# async def analyze_sentiment(text: str):
#     sentiment_analysis = pipeline("sentiment-analysis")
#     result = sentiment_analysis(text)
#     return {"text": text, "sentiment": result}

@app.post("/translate")
async def translateMessage(payload: TextModel): # 번역
    translator = googletrans.Translator()
    outStr = translator.translate(payload.text, dest='en', src='auto')
    return {
        "original msg": payload.text,
        "translate msg": outStr.text
    }

@app.post("/sentiment")
async def analyze_sentiment(payload: TextModel): # 감정분석
    # 명확한 model 사용
    sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analysis(payload.text)
    return {"text": payload.text, "sentiment": result}
