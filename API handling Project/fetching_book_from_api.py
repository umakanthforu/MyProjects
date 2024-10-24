import requests

url = "https://api.freeapi.app/api/v1/public/books/book/random"

response = requests.get(url)

bookdata = response.json()

def bookinfo():
    if bookdata["success"] and "data" in bookdata:
        country = bookdata["data"]["accessInfo"]["country"]
        etags = bookdata["data"]["etag"]
        return country, etags
    else:
        raise Exception ("Book not fetched.. !")
    
def main():
    try:
        countryinfo, etag = bookinfo()
        print(countryinfo, etag)
    except Exception as e:
        print(str(e))

main()