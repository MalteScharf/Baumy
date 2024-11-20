import socket
import datetime
import os

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


(client_socket, client_address) = server.accept()
print("Accepted Connecction from" + str(client_address))

while True:                                 # forever
    request = client_socket.recv(1024)    # receive data from client
    request = request.decode("utf-8")
    print("Request from Client: " + str(request))
    if not request: break                        # stop if client stopped
    client_socket.send(response.encode("utf-8"))
    print("Socket closed")


client_socket.close()
print("Socket closed")
