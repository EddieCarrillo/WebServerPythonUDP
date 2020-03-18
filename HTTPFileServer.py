#import socket module
from socket import *
import sys # In order to terminate the program

httpVersion = 'HTTP/1.1'

okPhrase = "OK"
okStatusCode = 200
goodStatusLine = f'{httpVersion} {okStatusCode} {okPhrase} \r\n'

missingFilePhrase = "Not Found"
missingFileStatusCode = 404
missingFileStatusLine = f'{httpVersion} {missingFileStatusCode} {missingFilePhrase} \r\n'

contentTypeHeaderLine = 'ContentType: text/html \r\n'

serverPort = 12346
#Set up a TCP socket.
serverSocket = socket(AF_INET, SOCK_STREAM)
#Associate the socket to this port
serverSocket.bind(('', serverPort))
#Start listening for TCP connections.
serverSocket.listen(1)
print('The server is listening for connections...')

while True:  
    #Establish a connection.  
    print("Ready to serve...")
    #Create a socket dedicated to this particular client.
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        #Get the URL and remove first forward slash in HTTP message
        filename = (message.split()[1])[1:]
        f = open(filename)
        outputData = f.read()   
        #Send one HTTP status line into the socket
        connectionSocket.send(goodStatusLine.encode())
        connectionSocket.send(contentTypeHeaderLine.encode())
        connectionSocket.send('\r\n'.encode()) #Data is comming up next.

        connectionSocket.send(outputData.encode())
        connectionSocket.send('\r\n'.encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found.
        connectionSocket.send(missingFileStatusLine.encode())
        connectionSocket.close()


serverSocket.close()
sys.exit()
