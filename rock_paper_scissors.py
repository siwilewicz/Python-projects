import sys

user1 = input("Who is player 1? ")
user2 = input("Who is player 2? ")
user1_answer = input("{}, do you want to choose rock, paper or scissors? ".format(user1))
user2_answer = input("{}, do you want to choose rock, paper or scissors? ".format(user2))

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Something went wrong! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer.lower(), user2_answer.lower()))