import tkinter as tk
from datetime import datetime
from enum import Enum
from tkinter import ttk
from socket import * 

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

    def set_state(self, choice):
        self.state = choice  

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

class Connection(): 
    def __init__(self, serverName, serverPort):
        #Server connection settings 
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((serverName, serverPort))

    def close(self):
        self.clientSocket.close()

    

class Message():
    def __init__(self):
        pass

def userinput(event, chat): 
    #print(text.get('2.0', '2.end'))
    #print(entrybox.get())
    try: 
        input = int(entrybox.get())
    except ValueError: 
        input = entrybox.get()
    
    chat.text.configure(state='normal')
    chat.text.insert(chat.counter.get_counter(), f'Your choice: {input}')
    chat.text.configure(state='disabled')
    entrybox.delete(0, 'end')
    chat.counter.increment()

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
chatbox = tk.Text(masterframe, height=25, width=25, bg='black', fg='#83c98c', font=("Helvetica", 10), state='disabled')
chatbox.grid(column=0, columnspan=2, row=1, sticky=('N', 'W,' 'E', 'S')) 
 

#User object
#user = User(count, chatbox)

#Chatroom object
chat = Chat(chatbox)

#Message object
message = Message()

#Connection obkect
#connection = Connection(serverName='localhost', serverPort=12000)


chat.displayMenu() 
 

#Entry textbook where users insert messages they want sent
entrybox = tk.Entry(masterframe, width=25)
entrybox.grid(column=0, row=2, sticky=('N', 'W', 'E', 'S')) 
entrybox.bind('<Return>', lambda event, chat=chat: userinput(event, chat))  


#Enter eventloop to allow users to interact
root.mainloop()  

"""sentence = input('Input lowercase sentence:')
connection.clientSocket.send(sentence.encode())
modifiedSentence = connection.clientSocket.recv(1024)
print(f'From server: {modifiedSentence.decode()}')
connection.close()"""