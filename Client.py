# Name : Jenil Bimal Desai
# UTA ID: 1001520245

# Citasions / References:
# http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# https://www.daniweb.com/programming/software-development/threads/481619/server-split-message-and-save-data-on-a-text-file
# http://codingnights.com/coding-fully-tested-python-chat-server-using-sockets-part-1/
# https://stackoverflow.com/questions/18685184/pep8-e501-line-too-long-error
# https://stackoverflow.com/questions/2261191/how-can-i-put-2-buttons-next-to-each-other?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://www.youtube.com/watch?v=hst3AWjxF5o
# http://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
# http://effbot.org/tkinterbook/listbox.htm

import time
import json
import sys
import tkinter as tk
# from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import messagebox
import socket
from time import sleep
from threading import Thread
# from SocketServer import ThreadingMixIn
from copy import copy
from Client_helper import ClientHelper


class Client:


    # def __str__(self):
    #     return self.
    #
    # def on_closing(self):
    #     """This function is to be called when the window is closed."""
    #     # ask to close the application.
    #     if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
    #         self.top.destroy()
    #         encoded_message = ClientHelper().encodemessage('has left the chat.')
    #         connect.client_socket.send(encoded_message.encode())
    #         connect.client_socket.close()
    #     else:
    #         pass

    # def receive(self,event=None):
    #     """Handles receiving of messages."""
    #     _last_time = 0
    #     while True:
    #         try:
    #             # receive message from server.
    #             print('before received message')
    #             self.msg = connect.client_socket.recv(connect.buffer_size).decode("utf8")
    #             print('msg received:', self.msg)
    #
    #             if self.msg == "coordinator":

                    # self.top = tkinter.Tk()
                    # self.top.title('coordinator')
                    # self.messages_frame = tkinter.Frame(self.top)
                    # self.my_msg = tkinter.StringVar()  # For the messages to be sent.
                    # self.my_msg.set("")
                    # self.scrollbar = tkinter.Scrollbar(self.messages_frame)  # To navigate through past messages.
                    # # Following will contain the messages.
                    # self.msg_list = tkinter.Listbox(self.messages_frame, height=15, width=80, yscrollcommand=self.scrollbar.set)
                    # self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
                    # self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
                    # self.msg_list.pack()
                    # self.messages_frame.pack()
                    # self.entry_field = tkinter.Entry(self.top, textvariable=self.my_msg)
                    # self.entry_field.bind("<Return>", self.sendMessage)
                    # self.entry_field.pack()
                    # self.send_button = tkinter.Button(self.top, text='send', command=self.sendMessage)
                    # self.send_button.pack()
                    # self.top.protocol("WM_DELETE_WINDOW", self.on_closing)
                    # self.top.mainloop()

                # elif self.msg == 'client':
                    # self.top = tkinter.Tk()
                    # self.top.title('client')
                    # self.messages_frame = tkinter.Frame(self.top)
                    # self.my_msg = tkinter.StringVar()  # For the messages to be sent.
                    # self.my_msg.set("")
                    # self.scrollbar = tkinter.Scrollbar(self.messages_frame)  # To navigate through past messages.
                    # # Following will contain the messages.
                    # self.msg_list = tkinter.Listbox(self.messages_frame, height=15, width=80,
                    #                                 yscrollcommand=self.scrollbar.set)
                    # self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
                    # self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
                    # self.msg_list.pack()
                    # self.messages_frame.pack()
                    # self.commit = tkinter.Button(self.top, text='Commit', command=self.commit)
                    # self.commit.pack()
                    # self.abort = tkinter.Button(self.top, text='Abort', command=self.abort)
                    # self.abort.pack()
                    # self.top.protocol("WM_DELETE_WINDOW", self.on_closing)
                    # self.top.mainloop()
                # else:
                    # msg = connect.client_socket.recv(self.buffer_size).decode("utf8")
                    # print('msg at else statement in client 91 line',self.msg)
                    # # print('msg received: ', msg)
                    # # split the header and body.
                    # msg_after_split = self.msg.split('\r\n\r\n')
                    # body = json.loads(msg_after_split[1])
                    # if _last_time == 0:
                    #     _last_time = body['time']
                    # time_passed = body['time'] - _last_time
                    # m, s = divmod(time_passed, 60)
                    # h, m = divmod(m, 60)
                    # body['message'].format(time="%d:%02d" % (m, s))
                    # self.msg_list.insert(tkinter.END, body['message'].format(time="%d:%02d" % (m, s)))
                    # _last_time = body['time']

                # split the header and body.
                # msg_after_split = msg.split('\r\n\r\n')
                # print('split message',msg_after_split[0])
                # body = msg_after_split
                # body = json.loads(msg_after_split[1])
                # print('body is: ',body)
                # print('body is: ', body)
                # count the time difference between 2 chats.
                # if _last_time == 0:
                #     _last_time = body['time']
                # time_passed = body['time'] - _last_time
                # m, s = divmod(time_passed, 60)
                # h, m = divmod(m, 60)
                # body['message'].format(time="%d:%02d" % (m, s))
                # #msg_list.insert(tkinter.END, body['message'].format(time="%d:%02d" % (m, s)))
                # _last_time = body['time']
    #         except OSError:  # Possibly client has left the chat.
    #             sys.exit()
    #
    # def sendMessage(self,event=None):
    #     pass
    #     # msg = self.my_msg.get()
    #     # encoded_msg = ClientHelper().encodemessage(msg)
    #     # print('encoded message from client: ',encoded_msg)
    #     # print('type of connect.client_socket.send(encoded_msg.encode())',type(connect.client_socket.send(encoded_msg.encode())))
    #     # connect.client_socket.send(encoded_msg.encode())
    #
    # def commit(self,event=None):
    #     pass
    #
    # def abort(self,event=None):
    #     pass
    #
    # def send(self,event=None):  # event is passed by binders.
        """Handles sending of messages."""
        # msg = my_msg.get()
        # my_msg.set("")  # Clears input field
        # encoded_message = ClientHelper().encodemessage(msg)
        # client_socket.send(encoded_message.encode())
        # if msg == "quit":
        #     client_socket.close()
        #     top.destroy()
        #     top.quit()


    # def on_closing():
    #     """This function is to be called when the window is closed."""
    #     # ask to close the application.
    #     if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
    #         top.destroy()
    #         encoded_message = ClientHelper().encodemessage('has left the chat.')
    #         client_socket.send(encoded_message.encode())
    #         client_socket.close()
    #     else:
    #         pass


# class Connection:

CO_TIME_OUT = 15
CLIENT_TIME_OUT = 10

class Timer(Thread):

    def __init__(self,timeout,func):
        Thread.__init__(self)
        self.timeout = timeout
        self.func = func

    def run(self):
        sleep(self.timeout)
        try:
            self.func()
        except:
            pass

# this is the client thread that has handled threads of clients.
class ClientThread(Thread):
    # at the start of the thrad it has socket and tkinter object.
    def __init__(self,client_socket):
        Thread.__init__(self)
        # self.ip = ip
        # self.port = port
        self.client_socket = client_socket
        self.tkinter = None
        # print
        # "[+] New server socket thread started for " + ip + ":" + str(port)

    # these message runs after thread has been created.
    def run(self):
        while True:
            # here the data has been received and the message has been encoded in HTTP format.
            data = self.client_socket.recv(2048).decode("utf-8")
            decode_data_from_server = data.split('\r\n\r\n')
            print('decode data:',decode_data_from_server[1])
            # encoded_data = ClientHelper().encodemessage(data)
            # here the data has been enter and stick at the last part of the tkinter.

            if decode_data_from_server[1] in ['ABORT','COMMIT']:
                # adding the votes to a list.
                self.tkinter.addVote(decode_data_from_server[1])
                # call process votes to check the votes.
                self.tkinter.processVote()
            elif decode_data_from_server[1] in ['GLOBAL_COMMIT' , 'GLOBAL_ABORT']:
                self.tkinter.addVote(decode_data_from_server[1])
                self.tkinter.processVote()
            else:
                self.tkinter.msg_list.insert(tk.END, decode_data_from_server[1])
                self.tkinter.set_string(decode_data_from_server[1])

            # print('in the run of client thread')
            # self.client_socket.send(message.encode())
            # time.sleep(10)
            # data = tcpClientA.recv(buffer_size).decode("utf8")
            # if data == 'exit':
            #     client_socket.close()
            #     sys.exit()
            # print('length of data is: ', len(data))
            # print('type of data is: ', type(data))
            # print('data is: ', data)
        self.client_socket.close()

    # helps to send data back to server in encoding format.
    def send_to_server(self, data):
        #encoded_request = ClientHelper().encodemessage(data)
        self.client_socket.send(data.encode())


# coordinator_receive = client_socket.recv(2048)
# while message != 'exit':
    # new_message = input('please enter something')

# co ordinator contains network thread and tkinter objects.
class Coordinator:
    # co ordinator contains network thread and tkinter objects
    def __init__(self, master, network_thread,id):
        self.network_thread = network_thread
        self.id = id
        self.network_thread.tkinter = self
        self.master = master
        # title of tkinter.
        master.title("co ordinator")
        # frame of tkinter.
        self.frame = tk.Frame(self.master)
        # message frame of tkinter.
        self.messages_frame = tk.Frame(self.master)
        # message of tkinter.
        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("")
        # scroll bar of tkinter.
        self.scrollbar = tk.Scrollbar(self.messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = tk.Listbox(self.messages_frame, height=15, width=80, yscrollcommand=self.scrollbar.set)
        # scrollbar of tkinter.
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # message list of tkinter.
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()
        # entry field of tkinter.
        self.entry_field = tk.Entry(self.master, textvariable=self.my_msg)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack()
        self.button1 = tk.Button(self.frame, fg="green", text='send', width=25, command=self.send)
        self.button1.pack(side=tk.RIGHT)
        self.frame.pack()
        self.votes = []
        self.voteResult = ''
        self.string_to_wtite = ''
        try:
            f = open('coordinator.txt', 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                self.msg_list.insert(tk.END,line)
        except:
            pass


    # send message to server.
    def send(self, event=None):
        # take a string message.
        string = self.my_msg.get()
        self.string_to_wtite = string
        # encode dtring in HTTP format.
        encoded_msg = ClientHelper().encodemessage(string)
        # print('encoded message from client: ', encoded_msg)
        # add at the end of the chatbox.
        self.msg_list.insert(tk.END,string)
        # print('type of connect.client_socket.send(encoded_msg.encode())',tcpClientA.send(encoded_msg.encode()))
        self.network_thread.send_to_server(encoded_msg)
        Timer(CLIENT_TIME_OUT,self.timeout).start()

    # add all the votes of the client.
    def addVote(self,vote):
        self.votes.append(vote)

    # count all the process votes.
    def processVote(self):
        # if length is three it checks for the commit and then send accordingly.
        if len(self.votes) == 3:
            commit = True
            for i in self.votes:
                if i == 'ABORT':
                    commit = False
            # if commit then send global_commit to server and then server broadcast it.
            if commit:
                glocal_commit = "GLOBAL_COMMIT"
                f = open('coordinator.txt', 'a+')
                f.write(self.string_to_wtite + '\n')
                f.close()
                self.voteResult = glocal_commit
                self.msg_list.insert(tk.END,glocal_commit)
                encoded_msg = ClientHelper().encodemessage(glocal_commit)
                self.network_thread.send_to_server(encoded_msg)
            # if aborts then send global_abort to server and then server broadcast it.
            else:
                glocal_abort = "GLOBAL_ABORT"
                self.voteResult = glocal_abort
                self.msg_list.insert(tk.END, glocal_abort)
                encoded_msg = ClientHelper().encodemessage(glocal_abort)
                self.network_thread.send_to_server(encoded_msg)
            self.votes = []

    def timeout(self):

        if not self.voteResult:
            glocal_abort = "GLOBAL_ABORT"
            self.voteResult = glocal_abort
            self.msg_list.insert(tk.END, glocal_abort)
            encoded_msg = ClientHelper().encodemessage(glocal_abort)
            self.network_thread.send_to_server(encoded_msg)
            self.votes = []

        # else:
        #     glocal_commit = "GLOBAL_COMMIT"
        #     self.voteResult = glocal_commit
        #     self.msg_list.insert(tk.END, glocal_commit)
        #     encoded_msg = ClientHelper().encodemessage(glocal_commit)
        #     self.network_thread.send_to_server(encoded_msg)

    # def startCoordinator(self):
    #         root = tk.Tk()
    #         app_coordinator = Coordinator(root)
    #         app_coordinator.mainloop()

        # self.newWindow = tk.Toplevel(self.master)
        # self.app = Demo2(self.newWindow)

# Clients contains network thread and tkinter objects.
class ClientTkinter:
    # Clients contains network thread and tkinter objects.
    def __init__(self, master,network_thread,id):
        self.master = master
        self.id = id
        self.network_thread = network_thread
        self.network_thread.tkinter = self
        master.title("Client")
        self.frame = tk.Frame(self.master)
        self.commit = tk.Button(self.frame, fg="green", text='Commit', command=self.commit)
        self.abort = tk.Button(self.frame, fg="red", text='Abort', command=self.abort)
        self.commit.pack(side=tk.RIGHT)
        self.abort.pack(side=tk.RIGHT)
        self.messages_frame = tk.Frame(self.master)
        self.scrollbar = tk.Scrollbar(self.messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = tk.Listbox(self.messages_frame, height=15, width=80, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()
        # self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        # self.quitButton.pack()
        self.frame.pack()
        self.voteResult = []
        self.string_to_commit = ''
        try:
            f = open('client{id}.txt'.format(id=self.id), 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                self.msg_list.insert(tk.END,line)
        except:
            pass

    def set_string(self,string_to_commit):
        self.string_to_commit = string_to_commit
        Timer(CO_TIME_OUT, self.timeout).start()

    # take response from button.
    def commit(self):
        commit_message = "COMMIT"
        # self.string = commit_message
        # append to the screen of tkinter.
        f = open('client.txt', 'a+')
        f.write(self.string_to_commit + '\n')
        f.close()
        self.msg_list.insert(tk.END,commit_message)
        # encode message
        commited_message = ClientHelper().encodemessage(commit_message)
        # send message to server.
        self.network_thread.send_to_server(commited_message)

    # take response from button.
    def abort(self):
        abort_message = "ABORT"
        # append to the screen of tkinter.
        self.msg_list.insert(tk.END, abort_message)
        # encode message
        aborted_message = ClientHelper().encodemessage(abort_message)
        # send message to server.
        self.network_thread.send_to_server(aborted_message)

    # set timeout of the client
    def timeout(self):
        # check for vote result.
        print('vote result',self.voteResult)
        if not self.voteResult:
            glocal_abort = "ABORT"
            # if it is abort it will send abort to client
            self.voteResult.append(glocal_abort)
            self.msg_list.insert(tk.END, glocal_abort)
            # encoded_msg = ClientHelper().encodemessage(glocal_abort)
            # self.network_thread.send_to_server(encoded_msg)
            # self.votes = []

    # add client votes to empty string
    def addVote(self,vote):
        self.voteResult.append(vote)

    # process client votes
    def processVote(self):

        if self.voteResult and self.voteResult[0] == "GLOBAL_ABORT":
            self.msg_list.insert(tk.END,self.voteResult[0])

        elif self.voteResult and self.voteResult[0] == "GLOBAL_COMMIT":
            f = open('client{id}.txt'.format(id=self.id), 'a+')
            f.write(self.string_to_commit + '\n')
            f.close()
            self.msg_list.insert(tk.END,self.voteResult[0])
        else:
            pass
    # def startClient(self):
    #     app_client = tk.Tk()
    #     client_obj = Client(app_client)
    #     client_obj.mainloop()

    # def close_windows(self):
    #     self.master.destroy()

# if coordinator_receive == 'coordinator':
#     cordinator_obj = Coordinator
#     cordinator_obj.startCoordinator()
#     # top = tkinter.Tk()
#     # top.title('coordinator')
#     # buttton = tkinter.Button(top,text='send',command=Client.sendMessage)
#     # buttton.pack()
#     # top.mainloop()
# elif coordinator_receive == 'client':
#     client_obj = ClientTkinter.startClient()
#     # top = tkinter.Tk()
#     # top.title('client')
#     # commit_buttton = tkinter.Button(top,text='commit',command=Client.commit)
#     # commit_buttton.pack()
#     # abort_button = tkinter.Button(top, text='commit', command=Client.abort)
#     # abort_button.pack()
# else:
#     pass




# c = Client()
        # # print('client is:',str(c))
        # self.receive_thread = Thread(target=c.receive)
        # self.receive_thread.start()


# class ClientThread(Thread):
#
#     def __init__(self,client_socket):
#         Thread.__init__(self)
#         # self.ip = ip
#         # self.port = port
#         self.client_socket = client_socket
#         # print
#         # "[+] New server socket thread started for " + ip + ":" + str(port)
#
#     def run(self):
#         while True:
#             data = self.client_socket.recv(2048)
#             print('in the run of client thread')

# assign the host and port.
host = 'JD'
port = 8080
address = (host, port)
buffer_size = 2048
# assign socket.
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect(address)
# print('after making connection')
data = tcpClientA.recv(2048).decode("utf-8")
root = tk.Tk()
# start network thread.
network_thread = ClientThread(client_socket=tcpClientA)
# print('network thread has been created.')
network_thread.start()
# create coordinator window.
data , id = data.split(';')
if data == 'coordinator':
    ui = Coordinator(master=root,network_thread=network_thread,id=id)
else:
    ui = ClientTkinter(master=root,network_thread=network_thread,id=id)
    # start tkinter.
root.mainloop()
# print('data is: ',data)







# connect = Connection()
# c = Client()

# # import Server
# # import Client
# import tkinter
#
#
# class Coordinator:
#
#     def __init__(self):
#         self.list_of_clients = []
#         self.message = 'vote for abort or commit'
#         # Client.client_socket.send(self.message.encode())
#         self.top = tkinter.Tk()
#         self.top.title('co-ordinator')
#         self.button = tkinter.Button(self.top,text="send",command="send")
#         self.button.pack()
#         self.top.mainloop()
#
#     def receiveMessageFromClients(self):
#         pass
#
#     def send(self):
#         pass
#
#
# c = Coordinator()



# if __name__ == '__main__':
#     main()


# print('client is:',str(c))
# receive_thread = Thread(target=connect)
# receive_thread.start()

# print ('connect has object like: ',connect.client_socket)

# create instace of the tkinter.
# top = tkinter.Tk()
#
# top.title("2 phase commit protocol")
#
# messages_frame = tkinter.Frame(top)
# my_msg = tkinter.StringVar()  # For the messages to be sent.
# my_msg.set("")
# scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# # Following will contain the messages.
# msg_list = tkinter.Listbox(messages_frame, height=15, width=80, yscrollcommand=scrollbar.set)
# scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# msg_list.pack()
# messages_frame.pack()
#
# entry_field = tkinter.Entry(top, textvariable=my_msg)
# entry_field.bind("<Return>", send)
# entry_field.pack()
# send_button = tkinter.Button(top, text="Send", command=send)
# send_button.pack()
#
# top.protocol("WM_DELETE_WINDOW", on_closing)
#
# # Socket and port name is defined and thread starts from here.
#
# tkinter.mainloop()
