import time
from tradingview_ta import TA_Handler, Interval, Exchange
from writer import DataWriter

from config import Config
from helpers import tv_analysis_to_dict
import datetime as dt

def fetch_date(interval):
    writer = DataWriter()
    writer.init_today_flder()

    config = Config.load()

    btc = TA_Handler(
        symbol=config.symbol,
        screener=config.screener,
        exchange=config.exchange,
        interval=interval
    )
    analysis = btc.get_analysis()

    writer.write_date(interval, tv_analysis_to_dict(analysis))

def wait():
    time.sleep(10 - (time.time() % 10))

last_fetched_5_m = None
last_fetched_15_m = None
last_fetched_1_h = None

while True:
    if (dt.datetime.now().minute % 5) == 0 and last_fetched_5_m != dt.datetime.now().minute:
        last_fetched_5_m = dt.datetime.now().minute
        fetch_date(Interval.INTERVAL_5_MINUTES)
        print("5 minute feched completed")
    if (dt.datetime.now().minute % 15) == 0 and last_fetched_15_m != dt.datetime.now().minute:
        last_fetched_15_m = dt.datetime.now().minute
        fetch_date(Interval.INTERVAL_15_MINUTES)
        print("15 minute feched completed")
    if dt.datetime.now().minute == 0 and last_fetched_1_h != dt.datetime.now().hour:
        last_fetched_1_h = dt.datetime.now().hour
        fetch_date(Interval.INTERVAL_1_HOUR)
        print("1 hour feched completed")
    wait()
