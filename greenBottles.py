#X Green Bottles
#Program counts down from a given number to 0 with the lines of 10 green bottles.
import time #Allows pauses

bottles = int(input("How many green bottles?")) #How many bottles

for x in range(bottles,0,-1): #Repeat until no bottles left
    print("{0} green bottle hanging on the wall.".format(x))
    time.sleep(2)
    print("{0} green bottle hanging on the wall.".format(x))
    time.sleep(2)
    print("And if 1 green bottle should acidentally fall,")
    time.sleep(2)
    print("There'll be {0} green bottles hanging on the wall.\n".format(x-1))
    time.sleep(3)
