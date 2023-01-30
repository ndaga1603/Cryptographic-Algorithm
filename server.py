# server
import hmac
import socketserver
import sqlite3
import json


def encript_password(password, key):
    encripted_password = hmac.new(key=key.encode(), msg=password.encode(),digestmod="sha256")
    return encripted_password.hexdigest()


def store_credentials(userneme, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (userneme, password))
    except sqlite3.OperationalError as e:
        cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (userneme, password))
    connection.commit()
    connection.close()


def validate_credentials(username, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user is not None and user[1] == password:
        return "User exist"
    return "User do not exist"
    

class PasswordManagementHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip().decode()
        credentials = json.loads(data)
        username = credentials["username"]
        password = credentials["password"]
        action = credentials["action"]
        key = "encription_key"
        encrypted_password = encript_password(password=password, key=key)
        if action == '1':
            store_credentials(userneme=username, password=encrypted_password)
            response = "User is successfully stored"
        if action == '2':
            response = validate_credentials(username=username, password=encrypted_password)
        self.request.sendall(response.encode())


server = socketserver.TCPServer(("0.0.0.0", 8000), PasswordManagementHandler)
server.serve_forever()
