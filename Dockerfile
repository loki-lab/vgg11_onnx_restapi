FROM python:3.8
LABEL authors="Loke"

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]