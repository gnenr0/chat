

import socket
import threading
import queue
import random
from pyfiglet import Figlet
import pyfiglet

img = pyfiglet.figlet_format("\t Welcome to the UDP chat room \n")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost" , random.randint(8000, 9000)))
name = input("What is your name? ")

def recieve():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target=recieve)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost" , 2525))

while True:
    message = input("")
    if message == "Quit!":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("localhost" , 2525))




