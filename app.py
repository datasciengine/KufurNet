import uvicorn
from fastapi import FastAPI

from kufurnet import KufurNet

app = FastAPI()
kufurnet = KufurNet()


@app.post("/check_profanity")
async def check_profanity(input_message: dict):
    """
    :param input_message: {"text":"hay amk yapacağınız işi sikim"}
    :return:
    """

    kufurnet.validate_input(input_message)

    text = input_message["text"]
    is_black, score, black_list = kufurnet.filter_analyze(text)

    if is_black:
        return {
            "status": True,
            "result": {"is_black": is_black,
                       "score": score,
                       "black_list": black_list
                       }}
    else:
        prediction = kufurnet.ml_analyze(text)
        return {
            "status": True,
            "result": {"is_black": True if prediction else False,
                       "score": 100 if prediction else 0,
                       "black_list": []
                       }}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)

    """
        1. BERT Modeli, 100 yorum, ort. 6 saniye.
        2. (Sinkaf + Toygar) SVM Modeli, 100 yorum, ms mertebesinde.
        3. Toygar(SVM) Modeli, 100 yorum, ms mertebesinde.
        4. Throff Veri (SVM) Modeli, 100 yorum ms mertebesinde.
        5. Filter Analyze (Rule Based)
    """
