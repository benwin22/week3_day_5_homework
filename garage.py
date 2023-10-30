# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

"""
create list for parkingSpaces
create a class for parking garage
create a number of spaces inside of garage
create a function that subtracts available tickets
this function should also show a decrease in parking spaces
ask the user to pay for parking 
show the amount to pay with an input with a timer
store the input in a variable
show the ticket is paid with a message "paid, 15min to exit"
update "currentTicket to dictiony as "paid" to TRUE
create a function that shows the paid user has exited
upon payment display "Thank You, have a nice day"
upon non-payment display input prompt for payment
call back the function upon payment display "thank you, nice day"
update parkingSpaces list to increase by 1 (add to parkingSpaces list)
update ticket list

need these attribute lists:

-tickets: int
-parkingSpaces: int
-currentTicket: int
"""
# num_spaces = range(1,5)
# print(list(num_spaces))

# parking_Spaces = [*range(1, 10, 1)]

# print(list(parking_Spaces))


class parking_Garage():
    def __init__(self, tickets, parkingSpaces, currentTicket ):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket    
#   decrementing
    def enter_garage(self):
        if self.parkingSpaces > 20:
            print("The garage is full! ")
            if self.parkingSpaces <= 20:
                print(f"There are {abs(self.parkingSpaces)} still available. ")
                                
        else:
            enter = int(input("How many tickets?  "))
            self.parkingSpaces -= enter
            if self.parkingSpaces < 20 :
                print(f"There are {abs(self.parkingSpaces)} still available. ")
                
#   incrementing
    def exit_garage(self):
        if self.currentTicket -= 1 :
            exit = (input("Please pay your ticket and say 'paid' "))
            self.parkingSpaces += exit
          
#   ticket
    def driver_ticket(self):
        
        print(f"You have paid, have a nice day ")
        print(f"Available Spaces: {abs(self.parkingSpaces)}")
        
    def check_available(self):
        print(f"There are {self.parkingSpaces} available. ")
        
def run():
    bens_garage = parking_Garage(20,20,1)

    while True:
        response = input("Would you like to buy, exit, check available spaces? ") 
        if response == "quit":
            print("Good luck finding a place")
            break
        elif response == "buy":
            bens_garage.enter_garage()
        elif response == "check":
            bens_garage.check_available()
        elif response == "exit":
            bens_garage.driver_ticket()
        else:
            print("Have a nice day ")
run()

            
        


   

