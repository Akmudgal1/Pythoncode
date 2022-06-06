user1=input("what is user 1 name:")
user2=input("what is user 2 name:")
user1_answer=input("user1 answer is"+user1)
user2_answer=input("user1 answer is"+user2)
if user1_answer==user2_answer:
    print("its a tie")
elif user1_answer=='rock':
    if user2_answer=='scissors':
        print("rock wins")
else:
        print("paper wins")
             	
elif user1_answer == 'scissors':
    if user2_answer == 'paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
    elif user1_answer == 'paper':
    if user2_answer == 'rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
    else:
    print("Invalid input! You have not entered rock, paper or scissors, try again.")
