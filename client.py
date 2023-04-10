import tkinter as tk
from datetime import datetime
from enum import Enum
from tkinter import ttk
from socket import * 
import pickle

class Count:
    def __init__(self):
        self.counter = 1.0 
    
    def increment(self):
        self.counter += 1.0

    def incrementBy(self, counter):
        self.counter += counter

    def get_counter(self):
        return self.counter
    
class User():
    def __init__(self):  
        self.username = None  
        self.color = None
        self.enabled = False
        self.state = 'normal'

    def set_state(self, choice):
        if choice == 1:
            self.state = 'report'
        elif choice == 2:
            self.state = 'request'
        elif choice == 3:
            self.state = 'quit' 

    def set_username(self, username):
        self.username = username
    
    def get_state(self):
        return self.state
     


class Chat():
    def __init__(self, text):
        self.text = text
        self.counter = Count()
    
    def displayMenu(self): 
        self.text.configure(state='normal')
        self.text.insert(self.counter.get_counter(), 
    '''Please select one of the following options:
        1. Get a report of the chatroom from the server.
        2. Request to join the chatroom.
        3. Quit the program.\n''')
        self.text.configure(state='disabled')
        self.counter.incrementBy(4.0) 

    def insertText(self, counter, message):
        self.text.configure(state='normal')
        self.text.insert(counter, message)
        self.text.configure(state='disabled')
        self.counter.increment()

class Connection(): 
    def __init__(self):
        #Server connection settings 
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        #self.clientSocket = socket(AF_INET, SOCK_STREAM)
        #self.clientSocket.connect((serverName, serverPort))
    
    def connect(self, serverName, serverPort, username):
        self.clientSocket.connect('localhost', 12000)

    def close(self):
        self.clientSocket.close()

    

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
    

def userinput(event, chat, user, connection): 
    #print(text.get('2.0', '2.end'))
    #print(entrybox.get())
    try: 
        input = int(entrybox.get())
        user.set_state(input) 
        chat.insertText(chat.counter.get_counter(), f'Your choice: {input}\n')
        entrybox.delete(0, 'end') 
        if input == 2:
            chat.text.configure(state='normal')
            chat.text.insert(chat.counter.get_counter(), f'Please enter username: ')
            chat.text.configure(state='disabled')
    except ValueError: 
        input = entrybox.get()
        if user.get_state() == 'request':
            chat.insertText('end', f'{input}\n') 
            entrybox.delete(0, 'end')
            message = Message()
            message.REPORT_REQUEST_FLAG = 0
            message.REPORT_RESPONSE_FLAG = 0
            #message.
 
    
    
    """
    user presses enter --> call userInput()
    I want menu to be popped up


    """

    """

    if user.get_state() == 'normal': 
        chat.text.configure(state='normal')
        chat.text.insert(chat.counter.get_counter(), f'Your choice: {input}\n')
        chat.text.configure(state='disabled')
        entrybox.delete(0, 'end')
        chat.counter.increment()
        if input == 1:
            chat.text.configure(state='normal')
            chat.text.insert(chat.counter.get_counter(), f'Please enter a username: {input}\n')
            chat.text.configure(state='disabled')
            entrybox.delete(0, 'end')
            chat.counter.increment()
        if input == 2:
            chat.text.configure(state='normal')
            chat.text.insert(chat.counter.get_counter(), f'Your choice: {input}\n')
            chat.text.configure(state='disabled')
            entrybox.delete(0, 'end')
            chat.counter.increment()
        if input == 3: #[20:36:06]  
            #1. if input is 3
            #2. need to connect
            #3. need to error check if username is used 
            chat.text.configure(state='joined')
            chat.text.insert(chat.counter.get_counter(), f'{datetime.now().strftime("%I:%M:%p")}: {input}\n')
            chat.text.configure(state='disabled')
            entrybox.delete(0, 'end')
            chat.counter.increment()
    elif user.get_state == 'joined':
        pass
    """
    
    

def insertText(text, string, index): 
    text.insert(index, string)
    index += 1.0
    return index 
 
#Setting room title, dimensions, configuring column/row 
root = tk.Tk()
root.title("Chatroom")
root.geometry('600x200') 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)   

"""
This is the frame before main frame
Users here will be prompted with 3 options to choose from:
    1. Get a report of the chatroom from the server
    2. Request to join the chatroom
    3. Quit the program
"""
 
#This is the main frame(chatroom) that user will interact 
masterframe = ttk.Frame(root)
#masterframe = tk.Frame(root, padx=5, pady= 5, bg='black')
masterframe.grid(column=0, row=0, sticky=('N', 'W,' 'E', 'S')) 

#configuring masterframe column/row
masterframe.columnconfigure(0, weight=1) 
masterframe.rowconfigure(1, weight=1) 
 
#Chatbox textbox that is disabled(user interaction disabled) 
chatbox = tk.Text(masterframe, height=25, width=25, bg='black', fg='#49ff38', font=("Helvetica", 10), state='disabled')
chatbox.grid(column=0, columnspan=2, row=1, sticky=('N', 'W,' 'E', 'S')) 
 

#User object
user = User()

#Chatroom object
chat = Chat(chatbox)

#Message object
message = Message()

#Connection object
connection = Connection()
#connection = Connection(serverName='localhost', serverPort=12000)


chat.displayMenu() 
 

#Entry textbook where users insert messages they want sent
entrybox = tk.Entry(masterframe, width=25)
entrybox.grid(column=0, row=2, sticky=('N', 'W', 'E', 'S')) 
entrybox.bind('<Return>', lambda event, chat=chat, user=user, connection=connection: userinput(event, chat, user, connection))  


#Enter eventloop to allow users to interact
root.mainloop()  

"""sentence = input('Input lowercase sentence:')
connection.clientSocket.send(sentence.encode())
modifiedSentence = connection.clientSocket.recv(1024)
print(f'From server: {modifiedSentence.decode()}')
connection.close()"""