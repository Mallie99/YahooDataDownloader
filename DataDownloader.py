import numpy as np
import pandas as pd
import yfinance as yf   # https://pypi.org/project/yfinance/
import openpyxl
import excel
import datetime as dt

from pandas import ExcelWriter

start_date = dt.date(2015, 12, 31)
end_date = dt.date(2022, 12, 31)
tickers = ('BB', 'GOOG', 'HYFM', 'SPY')

for ticker in tickers:
    df = yf.download(ticker, start=start_date, end=end_date)
    df.drop('Adj Close', axis=1, inplace=True)
    df = df.merge(yf.Ticker(ticker).dividends, how="left", on=["Date"])
    df.fillna(0, inplace=True)
    #df['Dividends'] = df['Dividends'].astype(float)
    df.loc[:, "Returns"] = np.log(
        (df['Close'] + df['Dividends']) / df['Close'].shift(1))
    format_dict = {'Close':'${:.2f}', 'Volume':'{:,}'}
    df = df.style.format(format_dict)
    with pd.ExcelWriter('C:/Users/malli/Desktop/Yahoo/Ticker Data.xlsx', mode='a', if_sheet_exists="replace", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name=ticker)

    #wb= openpyxl.load_workbook('C:/Users/malli/Desktop/Yahoo/Ticker Data.xlsx')
    #sheet=wb.get_sheet_by_name(ticker) 

    # writer = pd.ExcelWriter('C:/Users/malli/Desktop/Yahoo/Ticker Data.xlsx', engine='xlsxwriter')
    # #df.to_excel(writer, sheet_name=ticker)   

    # workbook = writer.book
    # worksheet = writer.sheets[ticker]
    #dec4_fmt = wb.add_format({'num_format': '#,##0.0000'})
    
    #sheet['H3'].number_format = '#,##0.0000'
    #sheet.set_column('H:H', 10, dec4_fmt)
    #ws[f'C{r}'].number_format ='"$"#,##0_);("$"#,##0)'