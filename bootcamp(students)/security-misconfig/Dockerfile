FROM python:3.10-slim

WORKDIR /app

COPY app /app
COPY static /static
COPY internal /internal
COPY flags /flags

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
