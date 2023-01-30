# Cryptographic-Algorithm for Password Management System

## A simple password management system that can store and validate user credentials.

### Features
- Encrypted password storage using sha256 encryption
- User validation

### Requirements
- Python 3
- SQLite
- hmac
- socket
- json
- Usage

* To run the system, start the server with the following command:
<code>python3 server.py</code>
* In another terminal, start the client with the following command:
<code>python3 client.py</code>
- The client will prompt you to enter a username, password, and an action (1 to store the user in the database or 2 to validate the user in the database). If you want to exit the process, type q as the username, password, or action.

### Note
The server is set to listen on all available interfaces on port 8000. If you want to change this, you can modify the <code> server = socketserver.TCPServer(("0.0.0.0", 8000), PasswordManagementHandler) </code> line in the server.py file.
