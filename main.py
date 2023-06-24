import os
import yahoo_fin.stock_info as si
import pandas as pd
from toolbox import database
from toolbox import ticker_retreival

storage_path = "/mnt/nvme1n1p1/"

database_path = os.path.join(storage_path, "database")
ticker_retreival.set_storage_path(database_path)


def main():

    # get all ticker info
    ticker_info = ticker_retreival.get_all_ticker_information()
    print(ticker_info)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
