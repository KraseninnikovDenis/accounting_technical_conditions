import peewee
from model import *

if __name__ == '__main__':
    
    try:
        db.connect()
        Users.create_table()
        Substations.create_table()
        DataApplications.create_table()
        StageApplication.create_table()
        RelationsAppSub.create_table()
    except peewee.InternalError as er:
        print(str(er))
