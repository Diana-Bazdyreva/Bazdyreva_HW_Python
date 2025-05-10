from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:1122@localhost:5432/QA"


def test_delete():
    db = create_engine(db_connection_string)
    with db.begin() as conn:
        sql = text("DELETE FROM subject WHERE subject_id = :id")
        result = conn.execute(sql, {"id": 118})

        assert result.rowcount > 0, f"No rows were deleted for ID {118}"
