# YahooDataDownloader

Yahoo data downloader with daily returns adjusted for dividends

Yahoo currently offers an adjusted time series of closing prices values. This series accounts for the payment of dividends and adjusts the previous asset prices downwards. This makes it easy to calculate the total return over a given holding period with dividends reinvested.
However, in backtesting quantitative strategies, these "adjusted" closing prices would not have actually been attainable.

For example, on the 27th Oct, 2022 the following data for "SPY" was observed
  Date	        Open	High	Low	  Close*	Adj Close**	Volume
  Oct 25, 2002	88.21	90.39	87.94	90.20	  61.44	      43,672,100

It would not have been possible to trade the ETF at $61.44. Any algorithm that tried to buy $1m worth of stock would have ended up with (1,000,000 / 90.20) 11,086 shares and NOT the (1,000,000 / 61.44) 16,276 that the adjusted data would suggest.

The code in this repository alters the adjusted close calculation by appending a new column of daily returns taking into account the ex-dividend dates and payments. (Data which is also sourced from Yahoo*). This new time series of return can then be compared to other asset returns as needed, whilst the original "Close" series can be used for backtesting trading algorithms and allocation.



* It's not my job to validate the accuracy of the dividend payout data...  
