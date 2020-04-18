###################################################################################################
# This python servers has three functions                                                         #
#   1: create a group of all users who submit a room code for the duration of the game            #
#   2: assign roles based on a card with only one person given the spy role                       #
#   3: signal all clients that the game has ended                                                 #
#                                                                                                 #
# Each of these tasks will be broken down into sub functions.                                     #
#   1: create a group of all users who submit a room code for the duration of the game            #
#       a: log all users who have submited a room code                                            #
#       b: have individual room codes                                                             # 
#       c: track the win condition and number of rounds a game lasts                              #
#   2: assign roles based on a card with only one person given the spy role                       #
#       a: each player is assigned only a single role - multiple people can have the same role    #
#       b: the spy role is assigned minumum of once a round                                       #
#       c: the person who was the spy last round is not the spy this round                        # 
#   3: signal all clients that the game has ended                                                 #
#       a: at the end of each round (every person has asked a question clockwise rotation)        #
#          the server asks if the non-spy players would like to guess who the spy is              #
#          if they guess correctly the game is won                                                #
#       b: at the end of each round; the server asks the spy client if they would like to guess   #
#          the location that we are at. If they guess correctly. They win the game.               #
###################################################################################################

#   2: each connection will be threaded for asycronouse connection handling
#      on a udp server
#   3: client security is handled using a jtw token authentication method

# other functions
#   1: sendUserCards
#   2: send end of game confirmation
#   3: send out user start game confirmation

# other variables or data 
#   1: start server with config.json
#   2: threaded each client connection to have asycronous connections 

from socket import *
from threading import Thread
import time

class messageObject: 
    def __init__(self, sender, recipient, message):
        self.sender = sender
        self.recipient = recipient
        self.message = message

    def getSender(self):
        return self.sender

    def getRecipient(self):
        return self.recipient

    def getMessage(self):
        return self.message

def main():
    print("Server for SpyFall Version 0.0.1")

    # Variable pool
    global server_socket
    SERVER_PORT = 5003

    try:
        cls()
        print("Starting..")

        server_socket = socket(AF_INET, SOCK_STREAM) # TCP server
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR)
        server_socket.bind(("", SERVER_PORT)) # bind to localhost serverport

        while True:
            print("Waiting for a connection...")
            client_socket = None
            try:
                client_socket, client_address = server_socket.accept()
                #start the thread
                Thread(target=listenToClient, args=[client_socket, client_address]).start()
            print("Connection acquired: {0}".format(str(client_address)))  # Notify a connection was made
    except KeyboardInterrupt:
        pass
    except Exception as e:
        cls()
        print(e)
        exit(-1)
    finally:
        cls()
        server_socket.close()
        print("Server for SpyFall Version 0.0.01 has closed..")
        exit(0) # close gracefully

def listenToClient(client_socket, client_address):
    # listen to the client for messages and handle accordingly 
    # has authentication built in

def sendTotalUserList():
    # send each user a list of all the players in play

def sendEndGameSignal():
    # sends the end game signal to all clients 

def sendNextTurnToClient(client_socket, client_address):
    # sends an individual client a indicator that its a next turn

if __name__ == "__main__":
    main()