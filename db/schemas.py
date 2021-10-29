from sqlalchemy import JSON, Boolean, Column, Integer, MetaData, String, Table


def get_exchange_symbols_table(metadata_obj: MetaData) -> Table:

    exchange_symbols_table = Table(
        "exchange_symbols",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("symbol", String(30)),
        Column("status", String(30)),
        Column("baseAsset", String(30)),
        Column("baseAssetPrecision", Integer),
        Column("quoteAsset", Integer),
        Column("quotePrecision", Integer),
        Column("quoteAssetPrecision", Integer),
        Column("baseCommissionPrecision", Integer),
        Column("quoteCommissionPrecision", Integer),
        Column("orderTypes", JSON(String(30))),
        Column("icebergAllowed", Boolean),
        Column("ocoAllowed", Boolean),
        Column("quoteOrderQtyMarketAllowed", Boolean),
        Column("isSpotTradingAllowed", Boolean),
        Column("isMarginTradingAllowed", Boolean),
        Column("permissions", JSON(String(30))),
    )

    return exchange_symbols_table
