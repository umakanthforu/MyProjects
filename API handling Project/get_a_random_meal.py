import requests

url = "https://api.freeapi.app/api/v1/public/meals/meal/random"

resource = requests.get(url)

masterdata = resource.json()

def randommeal():
    if masterdata["statusCode"] and "data" in masterdata:
        Typeoffood = masterdata["data"]["strArea"]
        category = masterdata["data"]["strCategory"]
        Ingredient1 = masterdata["data"]["strIngredient1"]
        Ingredient2 = masterdata["data"]["strIngredient2"]
        Ingredient3 = masterdata["data"]["strIngredient3"]
        Ingredient4 = masterdata["data"]["strIngredient4"]
        Instructions = masterdata["data"]["strInstructions"]
        return Typeoffood, category, Ingredient1, Ingredient2, Ingredient3, Ingredient4, Instructions
    else:
        raise Exception("Some Error has occured.. ")

def main():
    try:
        food, cat, ing1, ing2, ing3, ing4, inst = randommeal()
        print(f"Todays meal {food} of type {cat} and ingredients are {ing1}, {ing2}, {ing3} and {ing4}. \n Cooking Instructions are as follows : \n {inst}")
    except Exception as e:
        print("e")

main()
        
    
