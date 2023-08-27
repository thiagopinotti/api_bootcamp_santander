from peewee import *
import json

database = PostgresqlDatabase('teste', user='postgres', password='Tpg240482',
                           host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = database

# class Cliente(BaseModel):
#     nome = CharField()
#     telefone = CharField()
#     endereço = CharField()

# class Cerimonial(BaseModel):
#     nome = CharField()
#     telefone = CharField()
#     endereço = CharField()

# class Encomenda(BaseModel):
#     evento = CharField() #Aniversario ou Casamento ou Outro
#     evento_usr = CharField() 
#     cliente = ForeignKeyField(model=Cliente, backref='encomendas')
#     cerimonial = ForeignKeyField(model=Cerimonial, backref='encomendas')
#     data = DateField()
#     produto = CharField()
#     quantidade = IntegerField()
#     entrega = CharField() # entrega ou retirada
#     local_horario = CharField()
#     obs = CharField()

class Encomenda(BaseModel):
    nome = CharField()
    telefone = CharField()
    # data = DateField()
    cerimonial = CharField()
    local = CharField()

# database.create_tables([Cliente, Cerimonial, Encomenda])
database.create_tables([Encomenda])







 
