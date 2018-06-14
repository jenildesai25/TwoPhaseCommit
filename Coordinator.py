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

import tkinter as tk

class coordinator:
    def __init__(self, master):
        self.master = master
        master.title("co ordinator")
        self.frame = tk.Frame(self.master)
        self.messages_frame = tk.Frame(self.master)
        self.my_msg = tk.StringVar()  # For the messages to be sent.
        self.my_msg.set("")
        self.scrollbar = tk.Scrollbar(self.messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        self.msg_list = tk.Listbox(self.messages_frame, height=15, width=80, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.pack()
        self.messages_frame.pack()
        self.entry_field = tk.Entry(self.master, textvariable=self.my_msg)
        self.entry_field.bind("<Return>", self.send)
        self.entry_field.pack()
        self.button1 = tk.Button(self.frame,fg="green",text = 'send', width = 25, command=self.send)
        self.button1.pack(side=tk.RIGHT)
        self.frame.pack()

    def send(self,event=None):
        string = self.my_msg.get()


        # self.newWindow = tk.Toplevel(self.master)
        # self.app = Demo2(self.newWindow)

class Client:
    def __init__(self, master):
        self.master = master
        master.title("Client")
        self.frame = tk.Frame(self.master)
        self.commit = tk.Button(self.frame,fg="green",text='Commit',command=self.commit)
        self.abort = tk.Button(self.frame,fg="red",text='Abort',command=self.abort)
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

    def commit(self):
        pass
    def abort(self):
        pass
    # def close_windows(self):
    #     self.master.destroy()

def main():
    root = tk.Tk()
    app = coordinator(root)

    top = tk.Tk()
    client_obj = Client(top)
    root.mainloop()
    top.mainloop()

if __name__ == '__main__':
    main()