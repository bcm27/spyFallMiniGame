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
