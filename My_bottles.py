#!/usr/bin/env python3

from time import sleep

bstart=""
def setup(bstart):
    try:
        bstart=int(input("How many bottles of beer do you want to start with? Enter a number 1-99 or just press enter to start from 99\n"))
        if bstart>99:
            print("That's too many bottles of beer!")
            setup(bstart)
        if bstart<=0:
            print("That's not enough bottles of beer!")
            setup(bstart)
        if bstart=="":
            print ("Starting from 99..")
            sleep(2)
            bstart=99
            beer(bstart)
    except ValueError:
        if bstart=="":
            print ("Starting from 99..")
            sleep(2)
            bstart=99
            beer(bstart)
        else:
            print("Value Error: non numeric data")
            setup(bstart)
    except Exception:
            print("Unknown Exception: ")
            setup(bstart)
    if bstart!=None:
        beer(bstart)        

def beer(bstart):
    while bstart>0:
        if bstart > 1:
            word="bottles"
        else:
            word="bottle"
        print("{0} {1} of beer on the wall!\n{0} {1} of beer!\nTake one down and pass it around".format(bstart,word))
        sleep(2.5)
        bstart-=1
        if bstart>1:
            print("{} {} of beer on the wall!\n".format(bstart,word))
            sleep(2.5)
        elif bstart==1:
            print("{} {} of beer on the wall!\n".format(bstart,"bottle"))
            sleep(2.5)
        else:
            print("No more bottles of beer on the wall!\n")
            print ("Thanks for playing with me!")

if __name__ == "__main__":
    setup(bstart)