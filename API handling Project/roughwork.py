# import requests

# url = "https://api.freeapi.app/api/v1/public/youtube/channel"

# response = requests.get(url)

# masterdata = response.json()

# def youtubedata():
#     if masterdata["success"] and "data" in masterdata:
#         url = masterdata["data"]["info"]["snippet"]["customUrl"]
#         description = masterdata["data"]["info"]["snippet"]["description"]
#         return url, description
#     else:
#         raise Exception("Some error has occured")

# def main():
#     try:
#         yurl, ydescription = youtubedata()
#         print(yurl)
#         print(ydescription)
#     except Exception as e:
#         print(e)

# if __name__ == "__main__":
#     main()
# else:
#     pass

