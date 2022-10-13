import datetime
from lib2to3.pytree import Base
from peewee import *


db = SqliteDatabase('DB_TU.sqlite')

class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=20)
    last_name = CharField(max_length=20)


class Substations(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(20)
    voltag = CharField(15)
    

class DataApplications(BaseModel):
    id = PrimaryKeyField(null=False)
    folder_name = CharField(max_length=30)
    registation_user = ForeignKeyField(Users)
    data_create = DateTimeField(default=datetime.datetime.now)
    path_folder = CharField()
    application_number = CharField()
    power = FloatField()
    applicant_name = CharField()
    adres = CharField()
    voltag_class = CharField(max_length=20)
    substation_name = ManyToManyField(Substations)


class StageApplication(BaseModel):
    id = PrimaryKeyField(null=False)
    stage_number = CharField(max_length=5)
    status = CharField(default=('РЛЭ', 'заявитель', 'РЛЭ+заявитель'))
    basic_application = ForeignKeyField(DataApplications)


class RelationsAppSub(BaseModel):
    sub = ForeignKeyField(Substations)
    app = ForeignKeyField(DataApplications)


