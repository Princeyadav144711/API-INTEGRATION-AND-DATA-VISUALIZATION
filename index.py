import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Details
api_key = ""  
symbol = "GOOGL"  # company of Google

# Fetch data 
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full"
response = requests.get(url)
data = response.json()

# Check  'Time Series (Daily)' exists or not
if 'Time Series (Daily)' in data:
    # convert Pandas DataFrame
    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df.index = pd.to_datetime(df.index)
    df = df.rename(columns={"4. close": "Close"})

    # Convert to numeric
    df["Close"] = pd.to_numeric(df["Close"])

    # Plot stock 
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"])
    plt.title(f"{symbol} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()
else:
    print("Error: 'Time Series (Daily)'this key is not found in the API response.")
    print(data)
