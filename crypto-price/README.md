# Cryptocurrency Price Fetcher
#### This Python script fetches the current prices of selected cryptocurrencies from the CoinGecko API and displays them in a formatted table using Pandas.
### Features
- Fetches the current USD prices for Bitcoin, Ethereum, Dogecoin, and Tether.
- Formats the prices to include commas and two decimal points.
- Displays the results in a neatly formatted table.

### For use this program:
1. Create a docker image from the Dockerfile
```
   docker image build -t="crypto:1.0" .
```
2. Run a Docker Container from the image you build
```
   docker container run --rm crypt:1.1
```
