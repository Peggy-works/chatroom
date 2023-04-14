import time, sys, pickle
from threading import Thread
from socket import *
from datetime import datetime

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

"""def connection():
    message = Message()  
    while True:
        printPlease select one of the following options:
    1. Get a report of the chatroom from the server.
    2. Request to join the chatroom.
    3. Quit the program.
     
        
        user_input = input("Your choice: ") 
        if user_input == '1' or user_input == 1:
            pass
        if user_input == '2' or user_input == 2: 
            # User input 
            username = input("Please enter a username: ")
            
            # Setting message, pickling, sending
            message.set(0, 0, 1, 0, 0, 1, 0, 0, 0, 0, username, "", 0, 0) 
            
            data_send = pickle.dumps(message)
            print(f'Size of message object: {sys.getsizeof(data_send)}')
            clientSocket.send(data_send)

            # Wait for server Response
            waiting = True
            while waiting:
                try:   
                    response = clientSocket.recv(1024)
                    data_response = pickle.loads(response)
                    if data_response:
                        break
                except timeout:
                    pass

            # Server accept, exit loop 
            if data_response.JOIN_ACCEPT_FLAG:
                print("We breaking")
                break
            # Server reject, stay in loop
            elif data_response.JOIN_REJECT_FLAG:
                print(data_response.PAYLOAD) 
        elif user_input == '3' or user_input == 3:
            sys.exit()
        # Since user is accepted we can now send message to the server indefinitely, except for some conditions
        #while True:
            #sentence = input("input lowercase sentence:")
            #clientSocket.send(sentence.encode())
    while True:
        sentence = input("Insert text: ")
        clientSocket.send(sentence.encode())"""
            
"""
Consider sending a datetime object and when server recieves order it accordingly
actually try to make select work because this shit aint doing it
link: https://stackoverflow.com/questions/42222425/python-sockets-multiple-messages-on-same-connection
"""

def listen():
    while True:
        response = client_socket.recv(1024).decode()
        print(f'\n {response}')
            

# Host, port
HOST = 'localhost'
PORT = 12000 

# Creating new client socket and connecting via TCP
client_socket = socket(AF_INET, SOCK_STREAM)
print(f'Connecting to {HOST} at port: {PORT}')
client_socket.connect((HOST,PORT))

# Print menu options
print("""Please select one of the following options:
    1. Get a report of the chatroom from the server.
    2. Request to join the chatroom.
    3. Quit the program.""")

# user input
user_input = input("Your choice >> ")

# Setting up thread 
t = Thread(target=listen)
t.daemon = True
t.start()

# Creating message object
message = Message()

if user_input == 1 or user_input == '1':
    pass
elif user_input == 2 or user_input == '2':
    # User input 
    username = input("Please enter a username: ")
    
    # Setting message, pickling, sending
    message.set(0, 0, 1, 0, 0, 1, 0, 0, 0, 0, username, "", 0, 0) 
    
    # Pickling object 
    #data = pickle.dumps(message) 

    # Sending pickled message object to server
    client_socket.send(username.encode())
else:
    pass

while True:
    user_input = input(">> ")
    modified_message = datetime.now().strftime("[%H:%M]") + username + ": " + user_input
    client_socket.send(modified_message.encode())




# Connecting to server
#clientSocket = socket(AF_INET, SOCK_STREAM)  
#clientSocket.connect((HOST, PORT))



#connection()



#message = Message() 
#while True:
    #sentence = input("input lowercase sentence:")
    #clientSocket.send(sentence.encode())
    #modifiedSentence = clientSocket.recv(1024)
    #print(f'From server: {modifiedSentence.decode()}')
client_socket.close()