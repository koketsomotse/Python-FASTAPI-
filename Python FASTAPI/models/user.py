from sqlalchemy import Table, Column
from config.database import meta
from sqlalchemy.sql.sqltypes import Integer, String

users = Table(
    'Person', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(300)),
    Column('surname', String(300)),
    Column('email', String(300)),
    Column('password', String(300))

)
