from fastapi import FastAPI
from kufurnet import KufurNet

import uvicorn

app = FastAPI()
kufurnet = KufurNet()


@app.post("/check_profanity")
async def check_profanity(input_message: dict):
    """
    :param input_message: {'text' : 'hay amk'}
    :return:
    """

    kufurnet.validate_input(input_message)

    text = input_message["text"]
    is_black, black_list, score = kufurnet.filter_analyze(text)

    return {
        "status": True,
        "result": {"is_black": is_black,
                   "black_list": black_list,
                   "score": score}}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9000)

    """
        1. BERT Modeli, 100 yorum, ort. 6 saniye.
        2. (Sinkaf + Toygar) SVM Modeli, 100 yorum, ms mertebesinde.
        3. Toygar(SVM) Modeli, 100 yorum, ms mertebesinde.
        4. Throff Veri (SVM) Modeli, 100 yorum ms mertebesinde.
        5. Filter Analyze (Rule Based)
    """
