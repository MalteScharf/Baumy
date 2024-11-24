import socket
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, "Config.txt")
# Open the file
with open(file_path, "r") as file:
    server_ip = file.read()

server_ip = '192.168.178.38'
server_port = 8002

class BaumyClient:

    def __init__(self):
        self.server_ip = server_ip
        self.server_port = server_port

    def sendMessage(self, msg):
        #self.server_ip = server_ip
       # self.server_port = server_port

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.server_ip, self.server_port))


        client.send(msg.encode("utf-8"))

        response = client.recv(1024)
        response = response.decode("utf-8")
       # if not response: break
        print(response)
        client.close()



#client = BaumyClient()
#client.sendMessage("closesrv")