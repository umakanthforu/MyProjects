import requests

url = "https://api.freeapi.app/api/v1/public/meals?page=1&limit=10&query=rice"

response = requests.get(url)
maindata = response.json()

class recipelist:
    def recipes():
        if maindata["success"] and "data" in maindata:
            ingredient1 = maindata["data"]["data"][0]["strIngredient1"]
            ingredient2 = maindata["data"]["data"][0]["strIngredient2"]
            ingredient3 = maindata["data"]["data"][0]["strIngredient3"]
            ingredient4 = maindata["data"]["data"][0]["strIngredient4"]
            ingredient5 = maindata["data"]["data"][0]["strIngredient5"]
            instructions = maindata["data"]["data"][0]["strInstructions"]
            return ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, instructions
        else:
            raise Exception("Some unknown error has occured.")

    def main():
        try:
            ing1, ing2, ing3, ing4, ing5, inst = recipes()
            print(f"The list of ingredients required are {ing1}, {ing2}, {ing3}, {ing4}, {ing5} and Instructions to prepare are \n Instructions: {inst}")
        except Exception as e:
            print(e)
           

