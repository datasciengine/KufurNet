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

    return kufurnet.get_swears(comment)


if __name__ == "__main__":
    # Test verisi
    with open("data/curse_word.json", "r", encoding="utf-8") as file:
        test_data = json.load(file)

    results = {}

    # Verileri kontrol edip sonuçları "results" sözlüğüne kaydediyoruz
    for key, data in test_data.items():
        result = kufurnet.get_swears_1({key: data})
        results[key] = result[key]

    # Sonuçları JSON dosyasına kaydediyoruz
    with open("results.json", "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    # Web hizmetini çalıştırıyoruz
    uvicorn.run("app:app", host="0.0.0.0", port=9000)