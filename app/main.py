from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from .schemas import db, Quiz


app = FastAPI()
db.connect()
db.create_tables([Quiz,])
print('created')


class Questions(BaseModel):
    question_number: int


def parse_data(response):
    data = json.loads(response)
    data_dict = {}
    final_data = []
    exists_count = 0

    for question in data:
        if Quiz.select().where(Quiz.question_id == question["id"]):
            exists_count += 1
            continue
        data_dict["question_id"] = question["id"]
        data_dict["question_text"] = question["question"]
        data_dict["answer_text"] = question["answer"]
        data_dict["date"] = question["created_at"]
        final_data.append(data_dict)
        data_dict = {}
    if exists_count > 0:
        write_to_db(get_data(exists_count))
    return final_data


def get_data(count):
    url = f'https://jservice.io/api/random?count={count}'
    print(url)
    response = requests.get(url=url)
    final_data = parse_data(response.text)
    return final_data


def write_to_db(data):

    with db.atomic():
        for index in range(0, len(data), 50):
            Quiz.insert_many(data[index:index+50]).execute()

    if not db.is_closed():
        db.close()


@app.post('/question')
def get_item(item: Questions):
    write_to_db(get_data(item.question_number))
    last_record = Quiz.select().order_by(Quiz.id.desc()).get()
    response = {
        "id": last_record.question_id,
        "question_text": last_record.question_text,
        "answer_text": last_record.answer_text,
        "created_at": last_record.date
    }
    return response
