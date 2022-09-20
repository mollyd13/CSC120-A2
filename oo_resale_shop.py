from typing import Dict, Union, Optional
from computer import *
class ResaleShop:

    # What attributes will it need?
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    #sets initial item id at 0
    itemID = 0

    #constructs the resale shop object and creates inventory and itemID
    def __init__(self, inventory, itemID):
        self.inventory = inventory
    #creates empty dictionary for the inventory
        self.inventory = {}
        self.itemID = itemID

    # What methods will you need?

    #adds computer to inventory and updates the itemID
    def buy(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        print("Item", self.itemID, "bought!")

    #removes computer from inventory and prints message
    def sell(self):
        if self.itemID in self.inventory:
            del self.inventory[self.itemID]
            print("Item", self.itemID, "sold!")
        else: 
            # prints error message if item cannot be found
            print("Item", self.itemID, "not found. Please select another item to sell.")

    # prints the contents of the inventory
    def print_inventory(self):
        for computer in self.inventory:
            if self.inventory:
                    print(self.inventory)
            else:
                # prints that inventory is empty if there are no computers in it
                print("No inventory to display.")

    #locates the computer and refubishes it
    def refurbishCheck(self, computer):
        computer.refurbish(computer) # locate the computer
        print("Computer's Price and OS has been updated!")