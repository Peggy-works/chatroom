import tkinter as tk
from tkinter import ttk
from socket import * 
 
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
masterframe.grid(column=0, row=0, sticky=('N', 'W,' 'E', 'S')) 

#configuring masterframe column/row
masterframe.columnconfigure(0, weight=1)
masterframe.rowconfigure(1, weight=1)
 
#Chatbox textbox that is disabled(user interaction disabled) 
chatbox = tk.Text(masterframe, height=25, width=25, state='disabled')
chatbox.grid(column=0,row=1, sticky=('N', 'W,' 'E', 'S'))

entrybox = tk.Entry(masterframe, width=25)
entrybox.grid(column=0, row=2, sticky=('N', 'W', 'E', 'S')) 

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
print(f'From server: { modifiedSentence.decode() }')
clientSocket.close()
