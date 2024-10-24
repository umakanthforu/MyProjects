import requests

url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"

response = requests.get(url)
dogdata = response.json()

def random_dog():
    if dogdata["success"] and "data" in dogdata:
        dogname = dogdata["data"]["name"]
        dogheight = dogdata["data"]["height"]["metric"]
        dogweight = dogdata["data"]["weight"]["metric"]
        return dogname, dogheight, dogweight
    else:
        raise Exception("Some Error has occured..!")

# random_dog()
def main():
    try:
        dname, dheight, dweight = random_dog()
        print(f"The name of dog is {dname}, height is {dheight} and its weight is {dweight}")
    except Exception as e:
        print(e)

main()