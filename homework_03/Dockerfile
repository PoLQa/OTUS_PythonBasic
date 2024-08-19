FROM python:3.9-slim-buster

WORKDIR /app

COPY ./main.py /app
COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]