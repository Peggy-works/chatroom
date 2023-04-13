import time, sys, pickle
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

def connection():
    message = Message()  
    while True:
        print("""Please select one of the following options:
    1. Get a report of the chatroom from the server.
    2. Request to join the chatroom.
    3. Quit the program.
    """) 
        
        user_input = input("Your choice: ") 
        if user_input == '1' or user_input == 1:
            pass
        if user_input == '2' or user_input == 2: 
            # User input 
            username = input("Please enter a username: ")
            
            # Setting message, pickling, sending
            message.set(0, 0, 1, 0, 0, 1, 0, 0, 0, 0, username, "", 0, 0) 
            data_send = pickle.dumps(message)
            clientSocket.send(data_send)

            # Server Response
            response = clientSocket.recv(1024)
            data_response = pickle.loads(response)

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
        clientSocket.send(sentence.encode())
            

            

# Host, port
HOST = 'localhost'
PORT = 12000 

#user input
#user_input = None
#username = None
 
# Connecting to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST, PORT))

connection()



#message = Message() 
#while True:
    #sentence = input("input lowercase sentence:")
    #clientSocket.send(sentence.encode())
    #modifiedSentence = clientSocket.recv(1024)
    #print(f'From server: {modifiedSentence.decode()}')
clientSocket.close()