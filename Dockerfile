FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "src/main.py"]
ENTRYPOINT ["/entrypoint.sh"]
