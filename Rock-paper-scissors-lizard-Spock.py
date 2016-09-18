# Rock-paper-scissors-lizard-Spock template
import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if (name=='rock'):
        return 0;
    elif (name=='Spock'):
        return 1;
    elif (name=='paper'):
        return 2;
    elif (name=='lizard'):
        return 3;
    elif (name=='scissors'):
        return 4;
   


def number_to_name(number):
  
    if (number == 0):
        return 'rock';
    elif (number == 1):
        return 'Spock';
    elif (number == 2):
        return 'paper';
    elif (number == 3):
        return 'lizaed';
    elif (number == 4):
        return 'scissors';
    

def rpsls(player_choice): 
    
    
    # print a blank line to separate consecutive games
    print ('\n')
    # print out the message for the player's choice
    print ('Player chooses '+ player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    n_p = name_to_number(player_choice);
    # compute random guess for comp_number using random.randrange()
    n_c = random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    name_c = number_to_name(n_c)
    # print out the message for computer's choice
    print ('Computer chooses '+ name_c)
    # compute difference of comp_number and player_number modulo five
    diff = (n_c - n_p)%5
    diff = abs(diff)
    # use if/elif/else to determine winner, print winner message
    if(diff==1 or diff ==2):
        print ('Computer wins!')
    elif(diff==3 or diff==4):
        print ('Player wins!')
    elif(diff==0):
        print ("Player and computer tie!")
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
print('Enter Your choice \n "rock", "paper", "scissors", "lizard", "Spock" ')
s = input()
rpsls(s)



