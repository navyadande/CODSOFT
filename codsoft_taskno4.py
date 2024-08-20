import random
rock='''
    _______
---'   ____)
       (_____) 
       (_____)
---    (____)
   '__(___)
    
   '''
paper='''
    _______
---'   ____)____
          ______)
          _______)
        _______)
---_________)
            
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
       (____)
----__(___)   

'''   
game_images=[rock,paper,scissors]
user_choice=int(input("enter ur choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(game_images[user_choice])
if user_choice>=3 or user_choice<0:
    print("You entered invalid number, You lose.")
else:   
 computer_choice=random.randint(0,2)
 print("Computer choice")
 print(game_images[computer_choice])
 if computer_choice==user_choice:
    print("It's a draw")
 elif computer_choice>user_choice:
    print("You Lose")
 elif computer_choice<user_choice:
    print("You Win")  
 elif computer_choice==0 and user_choice==2:
    print("You Lose") 
 elif computer_choice==2 and user_choice==0:
    print("You Win")     
