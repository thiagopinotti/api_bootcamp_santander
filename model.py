from peewee import *
import json

database = PostgresqlDatabase('teste', user='postgres', password='Tpg240482',
                           host='localhost', port=5432)

# database = SqliteDatabase("db/dados.db")

class BaseModel(Model):
    class Meta:
        database = database

class Cliente(BaseModel):
    id = PrimaryKeyField()
    nome = CharField()
    cep = CharField()
    logradouro = CharField()
    bairro = CharField()
    localidade = CharField()
    uf = CharField()

database.create_tables([Cliente])







 
