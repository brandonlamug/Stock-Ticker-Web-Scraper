import pandas as pd
import yfinance as yf

print("Hello, I hope you're doing well. What ticker are you interested in researching today?")

entry = input("Choose from the following:  | AMD | AAPL | TSM |")

if entry == "AMD" or "amd":
    amd = yf.Ticker("AMD")
    infoamd = amd.info
    print("HERE'S YOUR INFO ON AMD, REBEL SCUM!")
    print(infoamd)
    for key, value in infoamd.items():
        print(key, ":", value)
elif entry == "AAPL" or "aapl":
    aapl = yf.Ticker("AAPL")
    infoaapl = aapl.info
    print("HERE'S YOUR INFO ON AAPL, REBEL SCUM!")
    print(infoaapl)
    for key, value in stockaaplinfo.items():
        print(key, ":", value)
elif entry == "TSM" or "tsm":
    tsm = yf.Ticker("TSM")
    infotsm = TSM.info
    print("HERE'S YOUR INFO ON TSM, REBEL SCUM!")
    print(infotsm)
    for key, value in infotsm.items():
        print("HERE'S YOUR DATA")
        print(key, ":", value)
else:
    print("What, can't you read? Give me something I can work with!")
    exit()