import socket
import datetime
import os
import sys
from LEDControllerFunctions import LEDFunctions
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, "Config.txt")

# Open the file
with open(file_path, "r") as file:
    server_ip = file.read()

port = 8002
response = "Request received"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen(0)
print("Server now listening on port " + str(port))

ledcounter = 0


while True: 
    (client_socket, client_address) = server.accept()
    print("Accepted Connecction from" + str(client_address))
    
    request = client_socket.recv(1024)    # receive data from client
    request = request.decode("utf-8")
    print("Request from Client: " + str(request))
    if not request: break    # stop if client stopped
    elif request == 'closesrv':
        client_socket.send(str("Server shutdown").encode("utf-8"))
        client_socket.close()
        print("Server closed")
        sys.exit()
    elif request == 'led':
        led = LEDFunctions()
        led.lightone(4, 255,255,255)
        client_socket.send(str("Led on").encode("utf-8"))

    elif request == 'next':
        led = LEDFunctions()
        led.lightone(ledcounter, 255,255,255)
        client_socket.send(str("Led on").encode("utf-8"))
        ledcounter +=1 ;
    

    elif request == 'led off':
        led = LEDFunctions()
        led.off()
        client_socket.send(str("Led off").encode("utf-8"))


    else: 
        client_socket.send(response.encode("utf-8"))

client_socket.close()
