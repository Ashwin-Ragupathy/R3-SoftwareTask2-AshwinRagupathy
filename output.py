import socket                                               # import socket so movement can be received from client

HOST = '127.0.0.1'                                          # declare socket's host
PORT = 25533                                                # declare socket's port

s = socket.socket()                                         # declare socket as s
s.bind((HOST, PORT))                                        # assign host and port to socket (Rover)
s.listen()                                                  # have Rover be the server that will accept
s, address = s.accept()                                     # get address of connection
print ('Rover is running with connection:', address)        # print address rover and client are connected with

while True:                                                 # run until socket is closed by a break
    movement = s.recv(1024).decode()                        # receive movement from client
    
    if (movement == "close"):                               # if movement says to close
         break                                              # break from loop
    
    print (movement)                                        # print movement from client 
s.close()                                                   # close socket