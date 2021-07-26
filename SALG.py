import random 
# Random module is imported to allocate positions randomly, By which in every new game there will be new board.
class Board():
    def __init__(self):
        # We create a 10 X 10 2D list to represent board.
        self.board = [[0]*10 for i in range(10)]
        for a in range(10):
            for b in range(10):
                if a%2==0:
                    # I try to mark a number for each point on board with respect to its position.
                    # The positions are marked in serial manner similar to the game. 
                    self.board[a][b] = [(10*a)+b+1,0]
                else:
                    self.board[a][b] = [(10*(a+1))-b,0]  
                
        # Initialistion of snake and ladder board
        for i in range(1,10,2):
            # Initialise random place for snake's head in every odd row ranging: 1->9
            Snake_head = random.choice([1,3,5,7,9])
            # Intitalise random bite value for snake's Bite in range: 0->(Bite Place-1)
            Snake_length = random.randint(1,i)
            # Initialise random place for snake's tail rangeing :0->Snake_head-1
            if Snake_length%2==0:
                # if tail is at odd row then random even column is allotted
                Snake_tail = random.choice([0,2,4,6,8])
            else:
                # if tail is at even row then random odd column is allotted
                Snake_tail = random.choice([1,3,5,7,9])    
        
            self.board[i][Snake_head][1]= self.board[i-Snake_length][Snake_tail][0]
        '''
        The summary of this part is to assign snakes at random odd rows and odd columns.
        the length of snake is random in range from 'minimum possible point-' on board to 'snake's head-1'.
        To avoid collisions between ladder's start and snake's head. if length of sanke is even then tail is 
        randomly assigned to "positon of head - length of snake"-row and even colums and vice-versa.

        '''                
        for j in range(0,9,2):
            # Initialise random place for ladder in even rows ranging: 0->8
            if j==0:
                Ladder_start = random.choice([2,4,6,8])
            else:    
                Ladder_start = random.choice([0,2,4,6,8])
            # Intitalise random length of ladder in range: 1->(9-Ladder_start)
            Ladder_length = random.randint(1,9-j)
            # Initialise random place for ladder's end rangeing :0->9
            if Ladder_length%2==0:
                Ladder_end = random.choice([1,3,5,7,9])
            else:
                if j+Ladder_length==9:
                    Ladder_end = random.choice([2,4,6,8])
                else:
                    Ladder_end = random.choice([0,2,4,6,8])   
            
            self.board[j][Ladder_start][1]= self.board[j+Ladder_length][Ladder_end][0]
                        
        '''
        The summary of this part is to assign ladder at random even rows and even columns.
        the length of ladder is random in range 'ladder start point + 1' to highest distance possible on board.
        To avoid collisions between ladder start and snake's head. if length of ladder is even then end is 
        randomly assigned to "positon of start + length of ladder"=row and odd colums and vice-versa.

        '''   

'''
This class creates a player profile with name as input taken and initial point as [0,0] on board
marked as 1. 

'''

class Players():
    def __init__(self,player_name):
        # Defines player name as input given
        self.Player_Name = player_name
        self.Player_Pos = 1
        #intial position on [0,0] equivalent to 1 on board we assume game starts form 1st position.


def rollDie(No_of_dies_rolled,die_point):
    if No_of_dies_rolled>=3:
    # Three 6 in row...oops You loose all of your points
        return [6,6,6]
    die_point.append(random.randint(1,6))
    # Random selection = Rolling Die
    if die_point[-1]==6:
        # if We get 6
        # Then we get another chance to roll die
        return rollDie(No_of_dies_rolled+1,die_point)
    return die_point

'''
This function works as Die rolled by player, it has a argument which defines the number of dies rolled by the player.
Three continous 6 results in cancellation of turn. Maximum number of turns for each player cannot exceed 3. 

'''
