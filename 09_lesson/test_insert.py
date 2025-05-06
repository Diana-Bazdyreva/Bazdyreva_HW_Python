from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:1@localhost:5432/postgres"



def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into subject (\"subject_title\") values (: new_title)")

    rows = db.execute(sql, new_title = 'Reflexing')
    1==1



