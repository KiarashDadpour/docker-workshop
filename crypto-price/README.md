# Cryptocurrency Price Fetcher
#### This Python script fetches the current prices of selected cryptocurrencies from the CoinGecko API and displays them in a formatted table using Pandas.
### Features
- Fetches the current USD prices for Bitcoin, Ethereum, Dogecoin, and Tether.
- Formats the prices to include commas and two decimal points.
- Displays the results in a neatly formatted table.

### Example Output
```bash
  Crypto  USD Price
 BITCOIN $67,655.00
DOGECOIN      $0.16
ETHEREUM  $3,791.42
  TETHER      $1.00

```
### For use this program:
1. Create a docker image from the Dockerfile:
```
   docker image build -t="crypto:1.0" .
```
2. Run a Docker Container from the image you build: 
```
   docker container run --rm crypt:1.0
```
Note:
If you have a issue in creating Dockerfile please change your dns to;
