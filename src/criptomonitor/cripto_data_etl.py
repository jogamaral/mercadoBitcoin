#!/usr/bin/python

import datetime
import logging
import sys
from typing import Any, Dict, List, Optional

import psycopg2.extras as p
import requests

from utils.db import WarehouseConnection
from utils.sde_config import get_warehouse_creds


def get_utc_from_unix_time(unix_ts: Optional[Any]) -> Optional[datetime.datetime]:
    return datetime.datetime.utcfromtimestamp(int(unix_ts)) if unix_ts else None


def get_coin_data(token: str) -> Dict[str, Any]:
    url = f"https://www.mercadobitcoin.net/api/{token}/ticker/"
    try:
        r = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"There was an error with the request, {ce}")
        sys.exit(1)
    return r.json().get("ticker")


def _get_coin_insert_query() -> str:
    return """
    INSERT INTO coin.cripto (
        token,
        high,
        low,
        vol,
        last_price,
        buy_price,
        sell_price,
        open_price,
        unix_time,
        utc_timestamp
    )
    VALUES (
        %(token)s,
        %(high)s,
        %(low)s,
        %(vol)s,
        %(last)s,
        %(buy)s,
        %(sell)s,
        %(open)s,
        %(date)s,
        %(utc_timestamp)s
    );
    """


def run() -> None:
    token_list = ["BTC", "ETH", "XRP", "USDC", "UNI"]
    for token in token_list:
        data = get_coin_data(token)
        data["utc_timestamp"] = get_utc_from_unix_time(data.get("date"))
        data["token"] = token
        print(data)
        with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
            curr.execute(_get_coin_insert_query(), data)


if __name__ == "__main__":
    run()
