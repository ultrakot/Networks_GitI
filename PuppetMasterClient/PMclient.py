# -*- coding: utf-8 -*-
import socket

# function 1 - get print Screen of the computer on Server Side
# get certain Commands to be send to the server side
#TAKE_SCREENSHOT




def process_command():
    """
    this function Process the Command before sending it to the server
    """
    cur_socket = socket.socket()
    cur_socket.connect(('127.0.0.1', 8820))  # slf computer?

    print "Hello, Please enter the command"
    message = raw_input('===>')
    print message
    # if message.lower() == 'take_screenshot':

    cur_socket.send(message)
    server_answer = cur_socket.recv(1024)
    print 'the server answered : ' + server_answer
    cur_socket.close()




# employee_bonus = 1000 if a > 50000000 else 0
#if __name__ == '__process_command__':
process_command()