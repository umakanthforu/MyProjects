with open("twinkle.txt", "r") as uma:
    if "twinkle" in uma.read().lower():
        print("Yes twinkle is available")
    else:
        print("Sorry, twinkle is not available")