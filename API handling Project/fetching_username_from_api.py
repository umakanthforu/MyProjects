import requests

## defining function to fetch username from url ###

# random URL taken from https://api.freeapi.app website for project purpose

def fetch_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    maindata = response.json() # maindata is a variable which stores response in json format
    # print(maindata)

    if maindata["success"] and "data" in maindata:
        # userdata = maindata["data"]
        username = maindata["data"]["login"]["username"]
        country = maindata["data"]["location"]["country"]
        return username, country
        # print(username, country)
    else:
        raise Exception("Failed to fetch userdata")

def main():
    try:
        username, country = fetch_data()
        print(username, country)
    except Exception as e:
        print(str(e))


main()

    