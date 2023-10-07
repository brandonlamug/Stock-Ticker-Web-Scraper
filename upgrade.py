import pandas as pd
import yfinance as yf

print("Hello, I hope you're doing well. What ticker are you interested in researching today?")

entry = input("Choose from the following:  | AMD | AAPL | TSM |")

if entry == "AMD":
    amd = yf.Ticker("AMD")
    stockinfo = amd.info
    print("HERE'S YOUR INFO ON AMD, REBEL SCUM!")
    print(stockinfo)
    for key, value in stockinfo.items():
        print(key, ":", value)
elif entry == "AAPL":
    aapl = yf.Ticker("AAPL")
    stockaaplinfo = aapl.info
    print("HERE'S YOUR INFO ON AAPL, REBEL SCUM!")
    print(stockaaplinfo)
    for key, value in stockaaplinfo.items():
        print(key, ":", value)
elif entry == "TSM":
    tsm = yf.Ticker("TSM")
    stocktsminfo = TSM.info
    print("HERE'S YOUR INFO ON TSM, REBEL SCUM!")
    print(stocktsminfo)
    for key, value in stocktsminfo.items():
        print("HERE'S YOUR DATA")
        print(key, ":", value)
else:
    print("What, can't you read? Give me something I can work with!")

