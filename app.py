from fastapi import FastAPI
from kufurnet import KufurNet

import uvicorn

app = FastAPI()
kufurnet = KufurNet()


@app.post("/analyze_profanity")
async def analyze_profanity(text: dict):
    """
    :param text: {'text' : 'hay amk'}
    :return:
    """
    return kufurnet.analyze(text)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000)
