FROM python:3.8
LABEL authors="MSAHIN & ACULHA"
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
WORKDIR /code
COPY ./* /code
COPY ./data /code/data
CMD ["python3", "app.py"]