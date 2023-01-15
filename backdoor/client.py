import socket

IP = "10.4.104.196"
PORT = 6060

ADDR = (IP ,PORT)

client = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
client.connect(ADDR)