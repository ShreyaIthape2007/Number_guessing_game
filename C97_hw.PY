import random

x=random.randint(1,9)

chances=5



print('Welcome to the number guessing game!')


while chances>=1:
    guess=int(input("Enter your guess! : "))

    if guess>x:
        print ('Sorry! Your number was too high. Try guessing a number less than ',guess)
        chances-=1
    elif guess<x:
        print('Sorry! Your number was too low. Try guessing a number greater than ',guess)
        chances-=1
    else:
        print('Yayy! You guessed correct!. The number was ',guess)
        break

    




