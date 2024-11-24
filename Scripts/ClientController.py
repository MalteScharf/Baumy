import socket
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, "Config.txt")

# Open the file
with open(file_path, "r") as file:
    server_ip = file.read()

print(server_ip)
server_port = 8002

msg = "off"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

client.send(msg.encode("utf-8"))

response = client.recv(1024)
response = response.decode("utf-8")
   # if not response: break
print(response)
client.close()