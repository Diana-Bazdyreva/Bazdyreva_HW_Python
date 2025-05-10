from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:1122@localhost:5432/QA"


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO subject (""subject_id,"
               "subject_title) VALUES ("":new_id, :new_title)")

    before_count_sql = text("SELECT COUNT(*) FROM subject")
    with db.connect() as conn:
        result_before = conn.execute(before_count_sql).fetchone()[0]

    with db.connect() as conn:
        conn.execute(sql, {"new_id": 118, "new_title": "Reflexing"})
        conn.commit()

    after_count_sql = text("SELECT COUNT(*) FROM subject")
    with db.connect() as conn:
        result_after = conn.execute(after_count_sql).fetchone()[0]

        assert result_after == result_before + 1
