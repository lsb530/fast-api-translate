from fastapi import FastAPI
import googletrans

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/translate/{msg}")
async def translateMessage(msg: str):
    translator = googletrans.Translator()

    outStr = translator.translate(msg, dest='en', src='auto')
    # print(f'{a=} {b=} {len(a)=}")
    result = {
        "original msg": msg,
        "translate msg": outStr.text
    }
    return result
    # return {"result": f"{outStr.text}"}
