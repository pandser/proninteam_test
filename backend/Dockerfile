FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]