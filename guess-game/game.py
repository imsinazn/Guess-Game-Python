import random
print("GUESS GAME")
print("Choose the type of game")
type_of_game = input("e = Easy (1-50) , m = Medium (1-100) , h = Hard (1-200)\nChoose: ")

if type_of_game in ['e' , 'm' , 'h']:
    print("Your challange was accepted !")
else:
    print("You entered a wrong letter!")
    exit()
    
if type_of_game == 'e':
    x = random.randint(1 , 50)
elif type_of_game == 'm':
    x = random.randint(1 , 100)
elif type_of_game == 'h':
    x = random.randint(1 , 200)
    
print("\nHint : Each guess is 10 point! If you make mistake you lose your points!")
count = int(input("Enter your count of Guesses = "))
point = count * 10
print(f"YOU HAVE {count} CHANCE")
print(f"Your starting points: {point}")
print("READY???")
while True:
    guess = int(input("Guess the number = "))
    if guess != x :
        count -=1
        point -= 10
        if count:
            if guess < 1 or guess > 200:
                print("your guess is out of range! ")
                break
            elif guess > x and guess - x <= 5:
                print(f"guess is over but very near! {count} is remaning ")
            elif guess > x and guess - x > 5:
                print(f"guess is over than secret number! {count} is remaning ")
            elif guess < x and x - guess <= 5:
                print(f"guess is lower but very near ! {count} is remaning ")
            elif guess < x and x - guess > 5:
                print(f"guess is lower than secret number! {count} is remaning ")

        else:
            print("YOU LOSE! 😈")
            print("START AGAIN!")
            break
    elif guess == x:
        print(f"Well down! the number was {x} ! 😁👍")
        print(f"Your point is = {point}")
        break