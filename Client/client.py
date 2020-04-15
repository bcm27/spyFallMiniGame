###################################################################################################
# This python client has three functions
#   1: clients can connect to a room using a 4 character code shared by the server host
#   2: clients get assigned cards from the server
#   3: clients can ask questions to a client in a theoretical clockwise circle
#   4: clients can guess at the end of each round who the spy is
#   5: clients can leave the game
###################################################################################################

# launch the gui application 

# connect to the server
#   1: handle server in coming messages
#       1: display the incoming card to the player
#       2: vote on which player to issue the guilty verdict too
#       3: end game incoming message
#       4: next round incoming message
#       5: send room assignment to server

def main():
    print("Starting Client GUI")

    # thread each gui window
    # launch the joinRoomGUI.py
    # after they choose a room we launch the gameGUI.py
    # depending on the state of the game we can display either the endGameGUI or cardDisplayGUI, etc.

def if __name__ == "__main__":
    main()