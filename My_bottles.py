#!/usr/bin/env python3

from time import sleep

bstart=""
while True:
    try:
        bstart=int(input("How many bottles of beer do you want to start with? Enter a number 1-99\n"))
        if bstart>99:
            print("That's too many bottles of beer!")
            continue
        if bstart<=0:
            print("That's not enough bottles of beer!")
            continue
    except ValueError:
        if bstart=="":
            print ("Starting from 99..")
            sleep(2)
            bstart=99
            break
        else:
            print("Value Error: non numeric data")
            continue
    except Exception:
            print("Unknown Exception: ")
            continue
    if bstart!=None:
        break        

def beer(bstart):
    while bstart>0:
        if bstart > 1:
            word="bottles"
        else:
            word="bottle"
        print("{0} {1} of beer on the wall!\n{0} {1} of beer!\nTake one down and pass it around".format(bstart,word))
        sleep(1)
        bstart-=1
        if bstart>1:
            print("{} {} of beer on the wall!\n".format(bstart,word))
            sleep(1)
        elif bstart==1:
            print("{} {} of beer on the wall!\n".format(bstart,"bottle"))
            sleep(1)
        else:
            print("No more bottles of beer on the wall!\n")
            print ("Thanks for playing with me!")

if __name__ == "__main__":
    beer(bstart)