from peewee import *



db = SqliteDatabase('database.db')


class Person(Model):
    name = CharField()

    class Meta:
        database = db

Person.create_table()