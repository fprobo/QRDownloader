#!/usr/bin/python

import sys
import os
import qrcode
import socket
import random
import SocketServer
import SimpleHTTPServer
from PIL import Image

def localIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def randPort():
    return random.randint(8000,9000)

def generateQR(data):
    qr = qrcode.QRCode(1)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def server(name):
    LOCAL_IP = str(localIP())
    PORT = randPort()

    web_dir = os.path.join(os.path.dirname(__file__), '/')
    os.chdir(web_dir)

    handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    try:
        serv = SocketServer.TCPServer(('', int(PORT)), handler)
    except PermissionError:
        print("Error!!")

    address = 'http://' + LOCAL_IP + ':' + str(PORT) + '/' + name
    generateQR(address).show()
    serv.serve_forever()

def main():
    server(sys.argv[1])

if __name__ == "__main__":
    main()
