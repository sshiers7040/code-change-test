testString = ""
searchChar = ""
charList = []
lastPosition = -1


while testString == "":
    testString = input("Please enter some text to search : ")

while len(searchChar) != 1:
    searchChar = input("Enter a character to search for :")

for x in range (len(testString)):
    if testString[x] == searchChar:
        charList.append(x-lastPosition)
        lastPosition = x

print ("I found {0} occurences of {1}".format(len(charList),searchChar))
