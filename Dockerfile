FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /quiz

# install dependencies

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--post", "8000"]