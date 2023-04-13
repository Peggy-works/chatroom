import time, sys, pickle, time
from socket import *

class Message():   
    REPORT_REQUEST_FLAG = None
    REPORT_RESPONSE_FLAG = None
    JOIN_REQUEST_FLAG = None
    JOIN_REJECT_FLAG = None
    JOIN_ACCEPT_FLAG = None
    NEW_USER_FLAG = None
    QUIT_REQUEST_FLAG = None
    QUIT_ACCEPT_FLAG = None
    ATTATCHMENT_FLAG = None
    NUMBER = None
    USERNAME = None
    FILENAME = None
    PAYLOAD_LENGTH = None
    PAYLOAD = None
    def set(self, REPORT_REQUEST, REPORT_RESPONSE, JOIN_REQUEST, JOIN_REJECT, JOIN_ACCEPT, NEW_USER, QUIT_REQUEST, QUIT_ACCEPT, ATTATCHMENT, NUMBER, USERNAME, FILENAME, PAYLOAD_LENGTH, PAYLOAD):
        self.REPORT_REQUEST_FLAG = REPORT_REQUEST
        self.REPORT_RESPONSE_FLAG = REPORT_RESPONSE
        self.JOIN_REQUEST_FLAG = JOIN_REQUEST
        self.JOIN_REJECT_FLAG = JOIN_REJECT
        self.JOIN_ACCEPT_FLAG = JOIN_ACCEPT
        self.NEW_USER_FLAG = NEW_USER
        self.QUIT_REQUEST_FLAG = QUIT_REQUEST
        self.QUIT_ACCEPT_FLAG = QUIT_ACCEPT
        self.ATTATCHMENT_FLAG = ATTATCHMENT
        self.NUMBER = NUMBER
        self.USERNAME = USERNAME
        self.FILENAME = FILENAME
        self.PAYLOAD_LENGTH = PAYLOAD_LENGTH
        self.PAYLOAD = PAYLOAD

def handleUser(connection, addr, users, user_count):
    print("In handleUser")
    message = Message()
    # Reject if 3 active users
    if user_count == 3:
        message.set(0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, "", 0, 'The server rejects the join request')
        data_send = pickle.dumps(message)
        connection.send(data_send)
        #time.sleep(30)
        #connection.close()
        return
    elif user_count < 3:
        response = connection.recv(1024)
        data = pickle.loads(response)
        #print(data.USERNAME)
        result = users.get(data.USERNAME)
        if not result:
            users[data.USERNAME] = {
                "IP": addr[0],
                "PORT": addr[1],
                "SOCKET": connection
            }
            user_count += 1
            username.append(data.USERNAME)
            message.set(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, data.USERNAME, "", 0, "USER has entered")
            data_send = pickle.dumps(message)
            connection.send(data_send)
        else:
            message.set(0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 , "", 0, "The server rejects the join request. Another user is using this username")
            data_send = pickle.dumps(message)
            connection.send(data_send)
    #print(users)

HOST = 'localhost'
PORT = 12000  

users = {}
username = []
user_count = 0

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(3)
#print("The server is ready to recieve")
#print(f'User count: {len(users)}')
#connectionSocket, addr = serverSocket.accept()
#handleUser(connectionSocket, addr, users, user_count)
while True:
    # Accepting new user connection and checking if username is taken
    connectionSocket, addr = serverSocket.accept()
    if connectionSocket:
        print(f'connectionSocket has something')
        print(connectionSocket)
    handleUser(connectionSocket, addr, users, user_count)
    # if condition for 1,2,3 users
    if len(users) == 1:
        print(users[username[0]]['SOCKET'].recv(1024).decode())
        #quit()
        pass
    elif len(users) == 2:
        print(users[username[0]]['SOCKET'].recv(1024).decode())
        print(users[username[1]]['SOCKET'].recv(1024).decode())
        pass
    elif len(users) == 3:
        pass
    """for user in users: 
        #print(users[user]['IP'])
        #print(users[user]['PORT'])
        #print(users[user]['Socket'])
        resp_message = users[user]['SOCKET'].recv(1024).decode()
        print(resp_message)"""
    #print(users)
    #print(len(users))
    #print(users)

        #users[addr[len(users)]] = 
    #print(f'Printing connectionSocket: {connectionSocket}')
    #print(f'Printing address: {addr[1]}')
    #response = connectionSocket.recv(1024).decode()
    #print(response)
    #capitalizedSentence = sentence.upper()
    #connectionSocket.send(capitalizedSentence.encode())
    #connectionSocket.close()
    
    #print("server close")