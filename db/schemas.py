from sqlalchemy import JSON, Boolean, Column, Integer, MetaData, String, Table
from sqlalchemy.orm import relationship


def get_exchange_symbols_table(Base) -> Table:
    class ExchangeSymbol(Base):
        __tablename__ = "exchange_symbol"

        id = Column(Integer, primary_key=True)
        symbol = Column(String(30), unique=True)
        status = Column(String(30))
        baseAsset = Column(String(30))
        baseAssetPrecision = Column(Integer)
        quoteAsset = Column(Integer)
        quotePrecision = Column(Integer)
        quoteAssetPrecision = Column(Integer)
        baseCommissionPrecision = Column(Integer)
        quoteCommissionPrecision = Column(Integer)
        orderTypes = Column(JSON(String(30)))
        icebergAllowed = Column(Boolean)
        ocoAllowed = Column(Boolean)
        quoteOrderQtyMarketAllowed = Column(Boolean)
        isSpotTradingAllowed = Column(Boolean)
        isMarginTradingAllowed = Column(Boolean)
        permissions = Column(JSON(String(30)))

    def __repr__(self):
        return f"Exch.Symbol: {self.id}, {self.symbol}, {self.status}"

    return ExchangeSymbol
