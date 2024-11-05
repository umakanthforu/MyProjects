import requests

url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"

resource = requests.get(url)

maindata = resource.json()

def bookinfo():
    if maindata["success"] and "data" in maindata:
        bookinfo = maindata["data"]["data"][4]["volumeInfo"]["description"]
        return bookinfo
    else:
        raise Exception("Some error has occured.")

def main():
    try:
        booki = bookinfo()
        print(booki)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
