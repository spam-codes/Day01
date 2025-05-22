import random

def computer():
   bot_choice = random.randint(1,3)
   if(bot_choice ==1):
       print("Computer Chose 'Stone'\n")
   elif(bot_choice==2):
       print("Computer Chose 'Paper'\n")
   elif(bot_choice==3):
       print("Computer Chose 'Scissors'\n")
   return bot_choice
   
def user():
   user_choice = int(input("\n\033[1;34mChoose One!\033[0m\nPress '1' for Stone\nPress '2' for Paper\nPress '3' for Scissors\n\nYour Choice :")) 
   if(user_choice ==1):
       print("\nYou Chose 'Stone'")
   elif(user_choice==2):
       print("\nYou Chose 'Paper'")
   elif(user_choice==3):
       print("\nYou Chose 'Scissors'")
   else :
       print("\n\033[33mInvalid Choice\033[0m\n")
       user()    
   return user_choice
   
def win():
    x = user()
    y = computer()
    if(x == y):
        print("\033[33mIt's a draw!\033[0m")
    elif(x==1 and y ==3) or (x==3 and y ==2):
        print("\033[32mHurrah! You Won!\033[0m")
    else:
        print("\033[31mYou Lose....\033[0m")    

def play_again():
    try_again = input("\nTry Again? (Y/N) :")
    if(try_again== "y" or try_again=="Y"):
        play()
    elif(try_again=="N" or try_again=="n"):
        print("\n\033[34mIt's Okay If You Don't Want To Play, bye...😔\033[0m")
    else:
        print("\nWhat Are You Doing Bro??, Just Type Y or N !")
        play_again()     
  
def play():
    win()
    play_again()

print("\033[1;35mWELCOME TO THE GAME\033[0m")
print("\033[1;36mGame Starts....\033[0m")        
play()    