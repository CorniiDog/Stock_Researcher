import os, time, datetime
import yahoo_fin.stock_info as si
import pandas as pd
from toolbox import database
from toolbox import ticker_retreival

storage_path = "/mnt/nvme1n1p1/"

database_path = os.path.join(storage_path, "database")
ticker_retreival.set_storage_path(database_path)

days_to_refresh = 5
def main():
    last_updated = 0
    while True:
        now = time.time()
        # If it is a new day, update the database
        if now - last_updated > 86400 * days_to_refresh:
            print("New Day, updating database")
            ticker_retreival.get_all_ticker_information()
            last_updated = now
        time.sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

