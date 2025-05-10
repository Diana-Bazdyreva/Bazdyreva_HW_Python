from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:1122@localhost:5432/QA"


def test_update():
    db = create_engine(db_connection_string)
    sql = text(
        "UPDATE subject SET subject_title = :new_title WHERE subject_id = :id")
    with db.connect() as conn:
        result = conn.execute(sql, {"new_title": "Secret_title", "id": 118})
        conn.commit()

    assert result.rowcount > 0
