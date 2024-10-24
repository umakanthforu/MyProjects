import random

def game():
    score = random.randint(1, 100)
    print(f" The new score is {score} ")
    return score

newscore = game()

with open("hiscore.txt", "r") as f:
    oldscore = int(f.read())
    print(oldscore, type(oldscore))
    print(newscore, type(newscore))

if newscore>oldscore:
    with open("hiscore.txt", "w") as f:
        f.write(str(newscore))
# else:
#     pass