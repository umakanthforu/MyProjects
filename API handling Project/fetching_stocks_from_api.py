import requests

url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"

response = requests.get(url)
# print(response)
stockdata = response.json()
# print(stockdata)

def stock():
    if stockdata["success"] and "data" in stockdata:
        stockname = stockdata["data"]["data"][1]["Name"]
        return stockname
    else:
        raise Exception("No stock found")

def main():
    try:
        stockinfo = stock()
        print(stockinfo)
    except Exception as e:
        print(e)

main()