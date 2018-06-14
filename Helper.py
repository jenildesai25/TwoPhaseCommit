# Name : Jenil Bimal Desai
# UTA ID: 1001520245

# Citasions / References:
# https://stackoverflow.com/questions/17501131/sending-txt-file-to-server-from-client-using-python-sockets
# https://stackoverflow.com/questions/7408647/convert-dynamic-python-object-to-json

from datetime import datetime
from json import dumps

# from Client import send
# from Client import *

# handle request of client.
class ServerHelper:
    # encode the request and send it.
    def decodeHTTPRequest(self, messsage):
        # message request body which accepts message.
        body = messsage
        # body contains message received from server.
        body_str = dumps(body)
        # body string dumps message in json format.
        method = "POST"
        # if method id post then in goes to this line.
        contentType = "application/plaintext; " + '\n' + "Accept-charset = UTF-8"
        # The User-Agent request header contains a characteristic string that allows the network protocol peers to
        # identify the application type, operating system, software vendor or software version of the requesting
        # software user agent.
        userAgent = "Chat Room"
        # sets host name to statis string.
        host = 'JD'
        # stores content length
        contentlength = len(body_str)
        date = date = datetime.utcnow().strftime('%a , %d  %b %Y %H:%M:%S GMT')
        # HTTP 1.1 is the latest version of Hypertext Transfer Protocol (HTTP), the World Wide Web application protocol
        # that runs on top of the Internet's TCP/IP suite of protocols.
        titleheader = 'HTTP/1.1 200 OK\r\n'
        # header contains all the informtion.
        headers = method + ' ' + titleheader + "Host: " + host + '\r\n' + "Content-Length: " + str(contentlength) + "\r\n" + "User-Agent: " + \
                  userAgent + "\r\n" + "Content-Type: " + contentType + '\r\n' +  'Date: ' + date
        # encode message and send if to receiver.
        encodedMessage = headers + "\r\n\r\n" + body_str

        return encodedMessage

