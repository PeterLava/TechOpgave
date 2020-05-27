import socket
import time
import threading


serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPClientSocket.setblocking(0)

def clientChat(UDPClientSocket):

    while True:
            time.sleep(0.1)
            msgFromClient = input("Client: ")
            bytesToSend = str.encode(msgFromClient)
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            time.sleep(0.1)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            if msgFromServer[0] == bytes(0xFE):
                isLost = True
                lostMsg = msgFromClient
                UDPClientSocket.sendto(bytes(0xFF), serverAddressPort)
                break
            else:
                msg = "Message from Server {}".format(msgFromServer[0])
                print(msg)
def counter():
    while True:
        autoMsg = bytes(0x00)
        UDPClientSocket.sendto(autoMsg, serverAddressPort)
        time.sleep(3)

def mainLoop():
    while True:
        autoMsg = bytes(0xFA)
        UDPClientSocket.sendto(autoMsg, serverAddressPort)
        clientChat(UDPClientSocket)
        time.sleep(0.1)

tr = threading.Thread(name="counter", target=counter)
tr2 = threading.Thread(name="mainLoop", target=mainLoop)
tr.start()
tr2.start()