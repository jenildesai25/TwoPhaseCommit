# Name : Jenil Bimal Desai
# UTA ID: 1001520245

# Citasions / References:
# https://www.geeksforgeeks.org/simple-chat-room-using-python/
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
# https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data
# https://stackoverflow.com/questions/30921399/datetime-fromtimestamp-vs-datetime-utcfromtimestamp-which-one-is-safer-to-use
# https://regex101.com/
# https://stackoverflow.com/questions/41761084/attributeerror-type-object-socket-has-no-attribute-socket

# import re
import json
# import threading
import time
import Client_helper
import socket

from threading import Thread
# from SocketServer import ThreadingMixIn


# import Client
import Coordinator
from Helper import ServerHelper
import tkinter
# from Client import *
# connected_list = []
VOTE_REQUEST = ["ABORT","COMMIT"]

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


class ClientThread(Thread):

    def __init__(self, ip, port,conn,active_clients):
        Thread.__init__(self)
        self.ip = ip
        # self.len_thread = len_thread
        self.port = port
        self.is_coordinator = len(active_clients) == 0
        self.id = len(active_clients)
        self.conn = conn
        self.active_clients = active_clients
        print("[+] New server socket thread started for " + ip + ":" + str(port))
        # self.clients = clients_list.append(port)

    def add_new_clients(self,newClient):
        return self.active_clients.append(newClient)


    def run(self):
        if self.is_coordinator:
            coordinator_message = 'coordinator;'+str(self.id)
            coordidator_request = self.conn.send(coordinator_message.encode())
        else:
            client_message = 'client;'+str(self.id)
            client_request = self.conn.send(client_message.encode())
        while True:
            data = self.conn.recv(BUFFER_SIZE).decode("utf8")
            # print(data)
            print(data)
            request_from_client = data.split('\r\n\r\n')
            # response_from_server = ServerHelper().decodeHTTPRequest(data)
            # print('response form server',request_from_client)
            #msg_after_split = request_from_client.split('\r\n\r\n')
            #print('message after split',msg_after_split)
            # print('active clients are',self.active_clients)
            if self.is_coordinator:
                self.broadcast_to_clients(request_from_client[1])
            else:
                self.send_to_coordinator(request_from_client[1])

            # clients = list_of_ports.append(conn[1])
            # print('clients is: ',clients)
            # self.broadcast(data,clients,prefix="")
            # handeling the case of the abort first
            # if data == VOTE_REQUEST[0]:
            #     # send abort to coordinator.
            #     abort_message = "ABORT"
            #     conn.send(abort_message.encode())
            # elif data == VOTE_REQUEST[1]:
            #     # send commit to coordinator.
            #     commit_message = "COMMIT"
            #     conn.send(commit_message.encode())
            # else:
            #     pass

            # MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            # if MESSAGE == 'exit':
            #     conn.close()
            #     break
            # conn.send(MESSAGE.encode())  # echo
    def broadcast_to_clients(self,message):
        # print('inside broadcast clients')
        encoded_string = Client_helper.ClientHelper().encodemessage(message)

        for active_client in self.active_clients:
            if not active_client.is_coordinator:
                active_client.conn.send(encoded_string.encode())

    def send_to_coordinator(self,message):
        encoded_string = Client_helper.ClientHelper().encodemessage(message)
        for active_client in self.active_clients:
            if active_client.is_coordinator:
                active_client.conn.send(encoded_string.encode())

    # def broadcast(self,data,name, prefix=""):  # prefix is for name identification.
    #     """ Broadcasts a message to all the clients. """
    #
    #     file = open('log.txt', '+a')
    #     file.write(json.dumps({'client_name': self.name, 'message': self.data}))
    #     file.write('\n')
    #     file.close()
    #     for sock in list_of_ports:
    #         print('sock is: ', sock)
    #         encoded_message = Helper().encodehttprequest(messsage=prefix + ' ({time}) - ' + self.data, timestamp=time.time())
    #         print("Server Broadcasted: ", type(encoded_message))
    #         sock.send(encoded_message.encode())

    # def __str__(self):
    #     return self.clients

connected_clients_dict = {}
addresses = {}
clients_list = []
# give host address of the server
# host = 'JD'
# # give port number of the server
# port = 8080
# # assign buffer size to store the data
# buffer_size = 1024
# threads = []
# # create socket to listen to client.
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # bind host and port
# # server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# server_socket.bind((host, port))
# c = Client()
list_of_ports = []
TCP_IP = 'JD'
TCP_PORT = 8080
BUFFER_SIZE = 2048  # Usually 1024, but we need quick response
# create socket and bind IP and PORT.
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []


while True:
    # thread starts listening.
    tcpServer.listen(4)
    # print("Multi threaded python server has started.")
    # restart_file = open('log.txt', 'r')
    # lines = restart_file.readlines()
    # for line in lines:
    #     print(line)
    (conn, (ip,port)) = tcpServer.accept()
    # print('server socket is: ',conn)
    # print("Waiting for connection...\n")

    # print('ip and port number',ip,port)
    # print (list_of_ports.append(port))
    newThread = ClientThread(ip,port,conn,threads)
    newThread.start()
    # print('after newThread.start method')
    threads.append(newThread)
    # print('threads are: ',threads,'connected clients is: ',ClientThread.name.__str__())
# for t in threads:
#     t.join()
    # thread has been initialized by upcoming statement.
    # ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    # ACCEPT_THREAD.start()
    # print('thread has been created.')
    # ACCEPT_THREAD.join()
    # server_socket.close()

