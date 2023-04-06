import tkinter as tk
from datetime import datetime
from tkinter import ttk
from socket import * 


def insertText(text, string, index):
    text.configure(state='normal')
    text.insert('1.0', string)
    text.configure(state='disabled') 
 
#Setting room title, dimensions, configuring column/row 
root = tk.Tk()
root.title("Chatroom")
root.geometry('500x500') 
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
masterframe = ttk.Frame(root, padding="5 5 5 5")
#masterframe = tk.Frame(root, padx=5, pady= 5, bg='#4f87f7')
masterframe.grid(column=0, row=0, sticky=('N', 'W,' 'E', 'S')) 

#configuring masterframe column/row
masterframe.columnconfigure(0, weight=1) 
masterframe.rowconfigure(1, weight=1)

#label atop the chatbox
label = tk.Label(masterframe, text='Chatroom', anchor='w', width=25, font=('Ubuntu Medium', 25))
label.grid(column=0, columnspan=2, row=0, sticky=('N', 'W,' 'E', 'S'))
 
#Chatbox textbox that is disabled(user interaction disabled) 
chatbox = tk.Text(masterframe, height=25, width=25, state='disabled')
chatbox.grid(column=0, columnspan=2, row=1, sticky=('N', 'W,' 'E', 'S'))
insertText(chatbox, 'hello world', '1.0')  

#Entry textbook where users insert messages they want sent
entrybox = tk.Entry(masterframe, width=25)
entrybox.grid(column=0, row=2, sticky=('N', 'W', 'E', 'S')) 

#Button widget to send message typed in entrybox
submit = tk.Button(masterframe, width=20)
submit.grid(column=1, row=2)

#Testing some datetime stuff
print(datetime.now())

#Enter eventloop to allow users to interact
root.mainloop()
 
#Server connection settings 
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(f'From server: {modifiedSentence.decode()}')
clientSocket.close()
