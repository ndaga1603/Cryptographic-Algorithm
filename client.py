# client 
import socket
import json


def get_server_response(username, password, action):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating socket
    sock.connect(("localhost", 8000)) # creating connection
    credatials = json.dumps({"username": username, "password": password, "action": action}) # craeting json data to send to the server
    sock.sendall(credatials.encode()) # sending creadential to the server
    response = sock.recv(1024).strip().decode() # receiving response from server
    sock.close() # close the connection
    return response

x = 0
while x == 0:
    print("To exit this proccess type 'q' as username or password")
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    action = input("Enter 1 (store user in databse) or 2 (validate user in database): ")
    if username == 'q' or password == 'q' or action == 'q':
        x = 1
    else:
        server_response = get_server_response(username=username, password=password, action=action)
        print(server_response)
  
   