from fastapi import FastAPI
from kufurnet.kufur_net import KufurNet

import uvicorn

app = FastAPI()
kufurnet = KufurNet()


@app.post("/profanity_checker")
async def profanity_checker(comment: dict):
    """
    :param comment: {'comment' : 'hay amk'}
    :return:
    """

    return kufurnet.get_swears(comment)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000)
