import socket                                   # import socket so data can be sent to rover
HOST = '127.0.0.1'                              # declare socket's host
PORT = 25533                                    # declare socket's port

import pygame                                   # import pygame for collecting keyboard input
import sys                                      # import sys to exit pygame without initialize video system error
pygame.init()                                   # initialize pygame
pygame.display.set_mode((200,200))              # create 200 by 200 window where data will be collected

speed = int (0)                                 # initialize speed of Rover as zero
movement = '[f0][f0][f0][f0]'                   # initialize movement of Rover as stationary

s = socket.socket()                             # declare socket as s
s.connect((HOST, PORT))                         # connect to socket located at host and port determined in declarations

while True:                                     # run until socket is closed by a break
    for event in pygame.event.get():            # get pygame events as they occur 
       
       if event.type == pygame.QUIT:            # if window is closed/pygame is quit
            movement = '[f0][f0][f0][f0]'       # set movement to stationary 
            s.send(movement.encode())           # tell Rover to be stationary by sending through socket
            s.send('close'.encode())            # tell Rover to close by sending through socket
            pygame.quit()                       # quit pygame
            sys.exit(0)                         # exit system without initialize video system error
            break                               # break from loop
        
       if event.type == pygame.KEYDOWN:         # if key is pressed
        
            if event.key == pygame.K_5:         # if key is pressed indicating speed (0-5)
                speed = 5                       # set speed to respective value (0-5) when pressed
                print("Speed: " + str(speed))   # print speed in console to show which key was pressed in video
            if event.key == pygame.K_4:
                speed = 4
                print("Speed: " + str(speed))
            if event.key == pygame.K_3:
                speed = 3
                print("Speed: " + str(speed))
            if event.key == pygame.K_2:
                speed = 2
                print("Speed: " + str(speed))
            if event.key == pygame.K_1:
                speed = 1
                print("Speed: " + str(speed))
            if event.key == pygame.K_0:
                speed = 0
                print("Speed: " + str(speed))

            if event.key == pygame.K_w:                                                                                                                                    # if key is pressed indicating direction (w = forward, a = left, s = backward, d = right)
                movement = '[f' + str(int ((speed/5)*255)) + '][f' + str(int ((speed/5)*255)) + '][f' + str(int ((speed/5)*255)) + '][f' + str(int ((speed/5)*255)) + ']'  # set movement to respective direction and speed
                s.send(movement.encode())                                                                                                                                  # send movement Rover should be doing through socket
                print("Direction: w")                                                                                                                                      # print direction chosen in console to show which key was pressed in video
            if event.key == pygame.K_a:
                movement = '[r' + str(int ((speed/5)*255)) + '][r' + str(int ((speed/5)*255))  + '][f' + str(int ((speed/5)*255)) + '][f' + str(int ((speed/5)*255)) + ']'
                s.send(movement.encode())
                print("Direction: a")     
            if event.key == pygame.K_s:
                movement = '[r' + str(int ((speed/5)*255)) + '][r' + str(int ((speed/5)*255)) + '][r' + str(int ((speed/5)*255)) + '][r' + str(int ((speed/5)*255)) + ']'
                s.send(movement.encode())
                print("Direction: s")     
            if event.key == pygame.K_d:
                movement = '[f' +str(int ((speed/5)*255)) + '][f' + str(int ((speed/5)*255)) + '][r' + str(int ((speed/5)*255)) + '][r' + str(int ((speed/5)*255)) + ']'
                s.send(movement.encode())
                print("Direction: d")     
                
            if event.key == pygame.K_c:         # if c key is pressed to close program
                print("Close Program and Rover")# print close in console to show which key was pressed in video
                movement = '[f0][f0][f0][f0]'   # set movement to stationary 
                s.send(movement.encode())       # tell Rover to be stationary by sending through socket
                s.send('close'.encode())        # tell Rover to close by sending through socket
                pygame.quit()                   # quit pygame
                sys.exit(0)                     # exit system without initialize video system error
                break                           # break from loop
s.close()                                       # close socket