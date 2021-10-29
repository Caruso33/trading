from dotenv import dotenv_values
from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.sql.expression import or_

from .schemas import get_exchange_symbols_table

config = dotenv_values(".env")


class DB:
    def __init__(self):
        db = config["db"]

        self.engine = create_engine(db, echo=False, future=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.mapper_registry = registry()

        self.Base = self.mapper_registry.generate_base()

    def get_connection(self):

        conn = self.engine.connect()
        conn.execution_options(isolation_level="AUTOCOMMIT")

        return conn

    def get_text(self, command: str):
        return text(command)

    def create_tables(self):

        ExchangeSymbol = get_exchange_symbols_table(self.Base)

        # keys = exchange_symbols_table.c.keys()

        # print(keys)

        self.mapper_registry.metadata.create_all(self.engine)

        return [ExchangeSymbol]


if __name__ == "__main__":
    db = DB()

    (ExchangeSymbol,) = db.create_tables()

    # insert
    # symbol1 = ExchangeSymbol(symbol="AAA")
    # symbol2 = ExchangeSymbol(symbol="BBB")

    # db.session.add(symbol1)

    # db.session.add_all([symbol1, symbol2])

    # db.session.commit()

    # read
    # exchange_symbols = db.session.query(ExchangeSymbol)
    # for exchange_symbol in exchange_symbols:
    #     print(exchange_symbol.symbol)

    # exchange_symbol = (
    #     db.session.query(ExchangeSymbol).filter(ExchangeSymbol.symbol == "AAA").first()
    # )
    # print(exchange_symbol.symbol)

    # exchange_symbols = db.session.query(ExchangeSymbol).filter(
    #     or_(ExchangeSymbol.symbol == "AAA", ExchangeSymbol.symbol == "BBB")
    # )
    # for exchange_symbol in exchange_symbols:
    #     print(exchange_symbol.symbol)

    # exchange_symbol_count = db.session.query(ExchangeSymbol).count()
    # print(exchange_symbol_count)

    # update
    # exchange_symbol = (
    #     db.session.query(ExchangeSymbol).filter(ExchangeSymbol.symbol == "AAA").first()
    # )
    # exchange_symbol.symbol = "CCC"
    # exchange_symbol = (
    #     db.session.query(ExchangeSymbol).filter(ExchangeSymbol.symbol == "CCC").first()
    # )
    # print(exchange_symbol.symbol)

    # delete
    # db.session.delete(exchange_symbol)
