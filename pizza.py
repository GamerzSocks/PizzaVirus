# pizza virus

#Global imports
import time
from datetime import datetime, timedelta
import random
import webbrowser
import os
import subprocess


print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣄⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠊⠉⠉⠉⠉⠉⣩⡷⠋⠉⠹⡛⢽⠢⣀⣀⡀⠀")
print("⢀⣀⣤⣴⠶⣾⣿⡿⠯⠯⣍⣙⣒⣲⠶⠶⠶⡿⢴⠧⠷⠒⣿⣏⠡⡤⠤⠯⡆")
print("⣿⣶⣒⡒⠛⠽⢯⣥⣶⣯⠭⡵⢊⣩⣭⣲⡂⡗⠈⠉⠉⠉⠉⡇⣼⣷⣿⣧")
print("⣮⣍⣛⡛⠛⠛⠛⠛⠛⠘⡾⣴⣿⣿⣿⣿⣧⡇⠀⠀⠀⢀⣰⣠⡽⣿⣿⠟")
print("⠾⠿⣶⣦⣭⣍⣹⣷⡄⡸⣹⣿⡿⣿⣻⣿⡿⠷⠶⠟⠛⠛⠉⠉⠓⠻⠟")
print("⠀⠀⠀⠉⠉⠁⠉⠛⠛⠛⠳⠿⢿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("")
print("-----------------------------")
print("")
print("")
print(" Domino's Windows App!")
print("")
print("")
print("-----------------------------")
# just to break up my spaghetti code



print("")
print("What pizza would you like to order?")
print("")
print("Margarita Pizza: Simply topped with lots of melted mozzarella goodness.")
print("Pepperoni Pizza: A Domino's classic. Slices of crispy pepperoni & creamy mozzarella.")
print("Hawaiian Pizza: A classic pairing of smoky leg ham & sweet pineapple pieces.")
print("")
pizza_selection = input("What pizza would you like to order? (NAME OF PIZZA eg. Pepperoni): ")
time.sleep(2)
print("")
print("Okay, 1 large " + pizza_selection + " pizza!")
time.sleep(2)


DeliveryAddress = input("Please insert a Delivery Address: ")

print("")
print("Ok, Delivering to " + DeliveryAddress + " !")
time.sleep(10)
print("")
print("We have recieved your order. We'll begin your live tracking ASAP.")
# "live" tracker
time.sleep(1)
print("")
print("Connecting to Store...")
print("")
time.sleep(5)
print("Recieved!")
print("")
print("We are making your pizza right now...")
time.sleep(50)
print("")
print("Putting your pizza in the oven...")
time.sleep(75)
print("")
print("Boxing it up...")
time.sleep(10)
print("")
print("Beginning delivery to " + DeliveryAddress + ".")

# ETA Calculations
CT = datetime.now()
ETA = CT + timedelta(minutes=5)
STRETA = ETA.strftime("%H:%M")

print("Estimated Arrival Time: " + STRETA)
time.sleep(300)

punishment_gen = (random.randint(0,2))


if punishment_gen == 1:
    for _ in range(5):
     url = "https://www.youtube.com/watch?v=48rz8udZBmQ"
     webbrowser.open(url)
     print("imagine not knowing that this was a virus lol.")

if punishment_gen == 0:
    print("Unfortunately, we have had to cancel your order for one " + pizza_selection + " pizza.")
    print("Sorry for the incovenience, Domino's Team.")


if punishment_gen == 2:
 for _ in range(10):
    punishment_gen = 2  # Replace this with your actual condition or variable

    if punishment_gen == 2:
        command_to_run = 'explorer'

        try:
            subprocess.run(command_to_run, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            filler = "filler"
 print("Have fun closing them file explorers! ;)")

