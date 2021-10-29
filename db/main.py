from dotenv import dotenv_values
from sqlalchemy import MetaData, create_engine, text

from .schemas import get_exchange_symbols_table

config = dotenv_values(".env")


class DB:
    def __init__(self):
        db = config["db"]

        self.engine = create_engine(db, echo=True, future=True)
        self.metadata = MetaData()

    def get_connection(self):

        conn = self.engine.connect()
        conn.execution_options(isolation_level="AUTOCOMMIT")

        return conn

    def get_text(self, command: str):
        return text(command)

    def create_tables(self):

        exchange_symbols_table = get_exchange_symbols_table(self.metadata)

        # keys = exchange_symbols_table.c.keys()

        # print(keys)

        self.metadata.create_all(self.engine)


if __name__ == "__main__":
    db = DB()

    conn = db.get_connection()

    db.create_tables()

    # try:
    #     result = conn.execute(get_text(command))
    #     print(result.all())

    # finally:
    #     conn.close()

    # conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    # conn.execute(
    #     text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
    #     [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    # )
