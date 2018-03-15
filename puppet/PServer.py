# -*- coding: utf-8 -*-
import socket
import time
import random
import datetime


server_socket = socket.socket()
# server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 8820))
server_socket.listen(1)
(client_socket, client_address) = server_socket.accept()


def main():
        data_from_client = client_socket.recv(1024)

        if data_from_client == "take_screenshot":
                pass  # get screen shot ,put it in a directory
                from PIL import ImageGrab
                im = ImageGrab.grab()
                im.save(r'C:\screen.jpg')

        elif data_from_client == "time":
                client_socket.send(str(datetime.datetime.now()))
        elif data_from_client == "name":
                client_socket.send("ragDoll")
        elif data_from_client == "rand":
                client_socket.send(str(random.randint(1, 42)))  # to string an random
        elif data_from_client == "out":
                client_socket.close()
                server_socket.close()

main()

client_socket.close()
server_socket.close()



# server_socket.close()



  # """
  #   puts the screen shot in a certain directory
  #
  #   lst = ['asas', 'aaaa', 'werewre', 'focus_file']
  #   print filter(isItTheFile, lst)
  #
  #   open_file = open('LoremIpsum.txt', 'w')
  #   open_file.write("lets write stuff here!")
  #   open_file.close()
  #   #create a directory
  #   target_file = file('LoremIpsum.txt', 'w')
  #   print target_file
  #   """
#
# if __name__ == '__main__':
#     main()