import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,tether&vs_currencies=usd"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    crypto_data = []
    for crypto, price_data in data.items():
        usd_price = price_data["usd"]
        formatted_price = "${:,.2f}".format(usd_price)
        crypto_data.append({"Crypto": crypto.upper(), "USD Price": formatted_price})

    df = pd.DataFrame(crypto_data)

    print(df.to_string(index=False))
else:
    print("Error :" , response.status_code)
