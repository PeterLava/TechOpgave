import socket
import sys
import time
from datetime import date
from datetime import datetime

today = datetime.now()
todaysDate = today.strftime("%d/%m/%Y %H:%M:%S")
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)
bufferSize = 1024
localIP = "127.0.0.1"
localPort = 20001
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Packages per second: ")
ammPck = 1/25
print("UDP server up and listening")

def chat(message, address):
    while (True):
        UDPServerSocket.settimeout(4)
        try:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
        except socket.timeout:
            print("Too slow...")
            try: 
                UDPServerSocket.sendto(bytes(0xFE), address)
                print("UDP server up and listening")
                break
            except:
                print("UDP server up and listening")
                break

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        UDPServerSocket.sendto(bytesToSend, address)
        time.sleep(ammPck)

while True:
    UDPServerSocket.setblocking(0)
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        if message == bytes(0xFA):
            f = open("logfil.txt", "a")
            f.write("Client has connected with IP: {} ".format(address))
            f.write(todaysDate)
            f.write("\n")
            f.close()
            chat(message, address)

    except:
        time.sleep(0.1)