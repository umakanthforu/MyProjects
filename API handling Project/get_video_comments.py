import requests

## to get video comments ####

url = "https://api.freeapi.app/api/v1/public/youtube/comments/cv-6bAeYsOY"

resource = requests.get(url)
comments = resource.json()

def read_comments():
    if comments["success"] and "data" in comments:
        num = int(input("Enter any number from 1 to 6 to check author details :"))
        author = comments["data"][num]["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        textdisplay = comments["data"][num]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        textoriginal = comments["data"][num]["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        return author, textdisplay, textoriginal
    else:
        raise Exception("Some error has occured.")

def main():
    try:
        authorname, tdisplay, toriginal = read_comments()
        print(f"{authorname} \n {tdisplay} \n {toriginal}")
    except Exception as e:
        print(e)

main()

