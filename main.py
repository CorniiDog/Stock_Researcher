import os
import yahoo_fin.stock_info as si
import pandas as pd
from toolbox import database
from toolbox import ticker_retreival

storage_path = "/mnt/nvme1n1p1/"

database_path = os.path.join(storage_path, "database")
ticker_retreival.set_storage_path(database_path)


def main():

    # Reference: https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b
    df1 = pd.DataFrame(si.tickers_sp500())
    df2 = pd.DataFrame(si.tickers_nasdaq())
    df3 = pd.DataFrame(si.tickers_dow())
    df4 = pd.DataFrame(si.tickers_other())

    # We convert to a list and then to a set to remove duplicates
    tickers = list(set(list(df1[0]) + list(df2[0]) + list(df3[0]) + list(df4[0])))
    tickers.sort()

    # Remove non-alphanumeric characters
    tickers = [x for x in tickers if x.isalnum()]

    # Save to database
    database.save("tickers", tickers)

    print("Done")


    # Test retreiving from database
    tickers = database.get("tickers")
    print(tickers)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
