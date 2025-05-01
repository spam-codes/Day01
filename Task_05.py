#importing random modzleto generate random number 
import random 
secret_number = random.randint(1,100)
attempts = 5
i=1
print("Welcome To The Number Guessing Game !\nYou Have 5 Attemps To Guess The Number:- ")
#Attempts and number input and checking
while(attempts):
  guess =int(input(f"\nAttempt {i} :Enter Your Guess - "))
  if guess ==secret_number:
     print("Congratulations! You Got It.")
     break
  elif guess<secret_number:
     print("Too Low")
  elif guess>secret_number:
     print("Too High")   
   
  attempts -= 1
  i+=1      

else:
    print(f"\n\nSorry The Number Was {secret_number}, Better Luck Next Time!")
