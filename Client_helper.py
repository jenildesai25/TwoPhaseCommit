# Name : Jenil Bimal Desai
# UTA ID: 1001520245

# Citasions / References:
# https://stackoverflow.com/questions/37016946/remove-b-character-do-in-front-of-a-string-literal-in-python-3
# https://stackoverflow.com/questions/28271051/datetime-to-date-format-in-python
# https://stackoverflow.com/questions/12362542/python-server-only-one-usage-of-each-socket-address-is-normally-permitted

import json
from datetime import datetime

# handle request of client.
class ClientHelper:
    # encode client message and send it.
    def encodemessage(self, request):
        # message request body which accepts message.
        #body = {'message':request
        # body contains message received from server.
        body_string = request
        # body string dumps message in json format.
        method = 'POST'
        # if method id post then in goes to this line.
        host = 'JD'
        # URL contains URL of the application.
        url = '/chat '
        # HTTP 1.1 is the latest version of Hypertext Transfer Protocol (HTTP), the World Wide Web application protocol
        # that runs on top of the Internet's TCP/IP suite of protocols.
        protocol = 'HTTP/1.1'
        # The User-Agent request header contains a characteristic string that allows the network protocol peers to
        # identify the application type, operating system, software vendor or software version of the requesting
        # software user agent.
        user_agent = '2 phase commit'
        # In responses, a Content-Type header tells the client what the content type of the returned content actually is
        content_type = 'text/plain'
        # It contains the content length of the body.
        content_length = len(body_string)
        # it sets date and time. here the format is UTC.
        date = datetime.utcnow().strftime('%a , %d  %b %Y %H:%M:%S GMT')
        # header contains all the informtion.
        header = method + url + protocol + "\r\n" + 'Host: ' + host + "\r\n" + 'User-Agent: ' + user_agent + "\r\n" \
                 + 'Content-Type: ' + content_type + "\r\n" + 'Content-Length: ' + str(content_length) + "\r\n" + \
                 'Date: ' + date
        # encode message and send if to receiver.
        encodedMessage = header + "\r\n\r\n" + body_string

        return encodedMessage
