# pizza virus
import time

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
#just to break up my spaghetti code



print("")
print("What pizza would you like to order?")
print("")
print("Margarita Pizza: Simply topped with lots of melted mozzarella goodness.")
print("Pepperoni Pizza: A Domino's classic. Slices of crispy pepperoni & creamy mozzarella.")
print("Hawaiian Pizza: A classic pairing of smoky leg ham & sweet pineapple pieces.")
print("")
pizza_selection = input("What pizza would you like to order? (NAME OF PIZZA eg. Pepperoni): ")
time.sleep(2)

print("Okay, 1 large " + pizza_selection + " pizza!")
time.sleep(2)

print("Please insert a Delivery Address:")
DeliveryAddress = input()

print("Ok, Delivering to " + DeliveryAddress + " !")
time.sleep(10)
print("We have recieved your order. We'll begin your live tracking ASAP.")
time.sleep(1)
print("Connecting to Store...)

