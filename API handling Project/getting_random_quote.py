import requests

url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"

response = requests.get(url)
quotedata = response.json()

def getquote():
    if quotedata["success"] and quotedata["data"]:
        quote = quotedata["data"]["content"]
        author = quotedata["data"]["author"]
        type = quotedata["data"]["tags"][0]
        return quote, author, type
    else:
        raise Exception("Some error has occured")
    
def main():
    try:
        pquote, pauthor, ptype = getquote()
        print(f"Quote of the day \n {pquote} \n {pauthor} \n {ptype}")
    except Exception as e:
        print(e)
    
main()