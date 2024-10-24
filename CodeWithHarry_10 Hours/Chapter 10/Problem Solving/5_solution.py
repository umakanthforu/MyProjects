class Train:
    def __init__ (uma):
        uma.tickets = 78
        uma.fare = 1384
    
    def avtickets(uma):
        print(f"the tickets available are {uma.tickets-1}")
        uma.tickets -=1
    
    def getfare(uma):
        print(f"the fare of ticket is {uma.fare}")

tr = Train()
tr.avtickets()
tr.getfare()
tr.avtickets()