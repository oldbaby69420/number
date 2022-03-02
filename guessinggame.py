import random 
number= random.randint(1,9)
chances=0
print ("just a number between 1 and 9")
while chances>5:
    guess= int(input("Enter your guess "))
    if guess == number:
        print("Congratulations! You win")
        break 
    elif guess<number:
        print("Guess higher")
        break
    else:
        print ("Guess lower")
        break
    chances+=1
if not chances<5:
    print ("You lose, The number is", number)
