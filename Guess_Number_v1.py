import random
import os
import msvcrt as m

def Menu():
    print("1)Easy")
    print("2)Normal")
    print("3)Hard")


def game(var, num):
    randm = random.randint(0, var)
    i = 1
    while True:
        if i < num:
            i = i+1
            inp = int(input("Guess a number: "))
            if inp == randm:
                print("you win!!!")
                m.getch()
                os.system('clear')
                break
            elif inp > randm:
                print("Try a smaller number")
            elif inp < randm:
                print("Try a larger number")
        else:
            print("Game Over")
            m.getch()
            os.system('clear')
            break


while (True):
    os.system('clear')
    Menu()
    inp = int(input("choose a difficulty: "))
    if inp == 1:
        print("### Easy mod ###")
        game(9, 11)
    elif inp == 2:
        print("### Normal mod ###")
        game(9, 6)
    elif inp == 3:
        print("### Hard mod ###")
        game(9, 4)
    else:
        print("Wrong number please try again!!!")
        os.system('clear')
