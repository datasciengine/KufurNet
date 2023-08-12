# KufurNet

Küfür, hakaret, sövgü, ofansif cümleleri başarılı şekilde tespit edebilmek için oluşturulmuş bir repodur. Küfür tespit konusunda repoları ve kara listeleri incelediğimizde yapılan çalışmaların oldukça yetersiz, maliyetli, başarısız ve kabul edilemez hatalarla dolu olduğunu gördük ve bu repoyu oluşturmaya karar verdik. 

Repoyu dilediğiniz gibi API olarak kullanabilir ve konteyner servis olarak koşturabilirsiniz.

<br>
![kufurnet fw](https://github.com/datasciengine/KufurNet/assets/90087613/43e12bcf-b26d-4009-b135-9259d1db44a3)
<br>

<b> FastAPI ile Servis Olarak Kullanım </b>

3 adımda kolayca API'yi yerel ağınızda kaldırabilirsiniz.

- python -m venv venv        # Venv oluşturun.
- .\venv\Scripts\activate    # Venv'i aktive edin.
- python app.py              # konsola yazmanız yeterlidir.

<b> API Kullanımı </b>

curl -X 'POST' \
  'http://localhost:9000/check_profanity' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{

"text" : "hay amk ulan"

}'

{
  "status": true,
  "result": {
    "is_black": true,
    "black_list": 0.67,
    "score": [
      "amk",
      "ulan"
    ]
  }
}

![image](https://github.com/datasciengine/KufurNet/assets/90087613/78c7d586-4a0c-4b82-a3f7-f844d237b9b3)


<b> Docker ile Servis Olarak Kullanım </b>

İki adımda kolayca konteyner servis olarak kullanın.

- docker build -t kufurnet .                               # image olarak build alın.
- docker run -d --name kufur_api  -p 9000:9000 kufurnet    # build aldığınız imajı konteyner olarak koşturun.
