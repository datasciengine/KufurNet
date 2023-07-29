from fastapi import FastAPI
from kufurnet.kufur_net import KufurNet
import json
import uvicorn

app = FastAPI()
kufurnet = KufurNet()


@app.post("/profanity_checker")
async def profanity_checker(comment: dict):
    """
    :param comment: {'comment' : 'hay amk'}
    :return:
    """
    pass
    #return kufurnet.get_swears(comment)


if __name__ == "__main__":

    with open("data/curse_word.json", "r", encoding="utf-8") as file:
        test_data = json.load(file)

    results = {}

    for key, data in test_data.items():
        result = kufurnet.get_swears_1({key: data})
        results[key] = result[key]

    with open("data/results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    #uvicorn.run("app:app", host="0.0.0.0", port=9000)
