#Create a cryptocurrency trading bot that can execute buy and sell orders on a cryptocurrency exchange. Implement strategies and algorithms for automated trading.

import ccxt
#BTC =BITCOIN
def get_binance_last_price(symbol):
    try:
        # Create an instance of the Binance exchange
        exchange = ccxt.binance()

        # Fetch ticker price for the trading pair
        ticker = exchange.fetch_ticker(symbol)

        # Extract the last price in USDT
        last_price_usd = ticker['last']

        # Assuming you have the current exchange rate for USD to INR
        # Replace 73.5 with the actual exchange rate
        exchange_rate_usd_to_inr = 73.5

        # Convert the last price to INR
        last_price_inr = last_price_usd * exchange_rate_usd_to_inr

        print(f'Last price of {symbol}: {last_price_usd} USDT')
        print(f'Last price in INDIAN RUPEES: {last_price_inr} INR')
    except ccxt.NetworkError as e:
        print(f'Network Error: {e}')
    except ccxt.ExchangeError as e:
        print(f'Exchange Error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Define the trading pair
symbol = 'BTC/USDT'

# Get and print the last price for the trading pair on Binance
get_binance_last_price(symbol)