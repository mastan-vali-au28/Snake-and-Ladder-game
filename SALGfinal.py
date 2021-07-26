import SALG 

# This function will check the presence of snake or ladder
# So its new postion can be evaluated.
# and return the position of player after its turn
def check(Position_player):
    x_axis_position= Position_player//10
    # Determining row on board by position.
    y_axis_position = Position_player%10-1
    # Determining column on board by position.
    if y_axis_position<0:
    # if column decreases beyond 0 means we have to change row.
        x_axis_position-=1 
        y_axis_position = 9
    if x_axis_position%2==1:
    # Because in odd rowss we travel in reverse order.
        y_axis_position = 9-y_axis_position

    if game.board[x_axis_position][y_axis_position][1]!=0:
    # This will work only if there is a sanke or ladder on that position.    
        return game.board[x_axis_position][y_axis_position][1]
        # returns the new postion for player coz of ladder or snake.
    return Position_player        
    # Otherwise, it will return original place of player.

def gameplay(Number_of_players):
    total_players = []
    # All players was handeled at a single place 
    for i in range(Number_of_players):
        print("Please enter Player's Name")
        total_players.append(SALG.Players(input()))
    Turn_of_player = 0
    # defines the turn of a particular player
    while True:
        points = SALG.rollDie(0,[])
        if sum(points)==18:
            print("Points after rolling die by "+ total_players[Turn_of_player].Player_Name +" -> 6 6 6")
            print("Turn Cancelled as you get 3 continous 6")
            points = 0
        else:
            print("Points after rolling die by "+ total_players[Turn_of_player].Player_Name +" -> ",*points)    
            points = sum(points)
        # Points gained after die was rolled by player
        position = total_players[Turn_of_player].Player_Pos
        # position reflects positon of a player on board
        # We only add points if total sum ranges less than or equal to 100.
        if position + points <=100:
            position+=points     
        else:
            print("The total Sum exceeds 100 you can't play this turn.")    
        new_position = check(position)
        if new_position<position:
            position = new_position
            print(total_players[Turn_of_player].Player_Name + " is bitten by a Snake. New position of",end = " ")
            print(total_players[Turn_of_player].Player_Name +" is ->" +str(position))
        elif new_position>position:
            new_position = new_position
            print(total_players[Turn_of_player].Player_Name + " climed a ladder. New position is ->",end = " ")
            print(total_players[Turn_of_player].Player_Name +"->" +str(position))  
        else:
            print("Position of "+ total_players[Turn_of_player].Player_Name+ " is " +"-> " +str(position))  
        # Now we will check if player is on end point or not .
        if position==100:
            # If Yes!, They print a congratulations note.
            total_players[Turn_of_player].Player_Pos = position
            print("Congratulations! "+str(total_players[Turn_of_player].Player_Name)+" is the Winner of this game.")
            # Along with the postions of all players.
            for k in range(Number_of_players):
                print("Final Position of "+total_players[k].Player_Name +" is -> "+str(total_players[k].Player_Pos)) 
            return
        # New position is assigned to the playing player.    
        total_players[Turn_of_player].Player_Pos = position
        # Now its turn for next player
        Turn_of_player+=1
        # If all player have their turn then cycle repeats util we have a winner
        if Turn_of_player>=len(total_players):
            Turn_of_player = 0
# An instance of class is created 
game = SALG.Board()
#Representation of Board
for row in reversed(range(10)):
    for column in range(10):
        print(game.board[row][column],end = " ")
    print()

print("Please enter the number of players participating in the Game.")   
Number_of_players = int(input())
# Number of player will play Game.
gameplay(Number_of_players)            
