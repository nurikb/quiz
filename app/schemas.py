from peewee import *
from .db_settings import DB_HOST, DB_NAME, DB_PASS, DB_USER, DB_PORT

db = PostgresqlDatabase(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


class Quiz(Model):
    question_id = IntegerField(unique=True)
    question_text = TextField(null=True)
    answer_text = TextField(null=True)
    date = DateField(null=True)

    class Meta:
        database = db


