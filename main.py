# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
#from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

#imports computer and resale object
from computer import *
from oo_resale_shop import *

def main():
    #initializes the resale shop
    resaleshop = ResaleShop([],0)
    #creates a computer object
    computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    print("Buying")
    print("Adding to inventory...")
    # adds a computer to the inventory
    resaleshop.buy(computer)
    # prints updated inventory
    resaleshop.print_inventory()
    # refurbishes the computer
    resaleshop.refurbishCheck(computer)
    # removes computer from inventory
    resaleshop.sell()
    # prints updated inventory
    resaleshop.print_inventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()