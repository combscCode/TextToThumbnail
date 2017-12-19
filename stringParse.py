import random
import sys
import os

#read in the title 
str1 = open('input.txt', 'r+').read()

#split the title separated by white space 
#save as a LIST named title 
title = str1.split()
print(title)

#first, we need to find the index of the dash,
#so that everything before it as the tournament name 
indexDash = 0;
for i in range(0, len(title)):
    if(title[i] == "-"):        #it is important that the dash is separated by WHITESPACE or this code will not work
        indexDash = i
        break

#once we know the index of the dash, we know that everthing before it is the tournament name
tournamentName = ""

#add whitespace inbetween each word
for i in range(0, indexDash - 1):
    tournamentName += title[i] + " "
tournamentName += title[indexDash - 1]

#delete the tournament name AND DASH from the title
#we will create the title at the end
for i in range(0, indexDash+1):
    title.remove(title[0])

#CREATE FUNCTION FOR PLAYER TAG,CHARACTER????


#next, we want to find the index of the first parenthesis, so that
#we know how long player 1's tag is
indexPar = 0
for i in range(0, len(title)):
    if(title[i][0] == "("):     #again, it is very important that there is WHITESPACE before '('
        indexPar = i
        break

#save player1Tag including whitespace between words
#then, remove it from title
player1Tag = ""
for i in range(0, indexPar-1):
    player1Tag += title[i] + " "
player1Tag += title[indexPar-1]
title.remove(title[0])


#print(player1Tag[1:len(player1Tag)-2])
#for reference of how to index

#now, we need a series of if statements because inputting the character's
#color is OPTIONAL
player1Char = ""
player1Col = ""
#if color is not provided, then the first element in the list will begin with '('
#AND end with ')'
if(title[0][len(title[0])-1] == ")"):
    #index from the 2nd element to the 2nd to last element
    player1Char = title[0][1:len(title[0])-1]
    player1Col = "Neutral"
    #remove only the one element
    title.remove(title[0])
#if color if provided, then the second element will end with ')'
elif(title[1][len(title[1])-1] == ")"):
    player1Col = title[0][1:]
    player1Char = title[1][0:len(title[1])-1]
    #remove two elements for color and char
    title.remove(title[0])
    title.remove(title[0])
else:
    print("ERROR: invalid input")


#REMOVE the 'vs'
title.remove(title[0])


#Now, do the same for player2, might put in function for efficiency
player2Tag = ""
for i in range(0, indexPar-1):
    player2Tag += title[i] + " "
player2Tag += title[indexPar-1]
title.remove(title[0])


#now, we need a series of if statements because inputting the character's
#color is OPTIONAL
player2Char = ""
player2Col = ""

#if color is not provided, then the first element in the list will begin with '('
#AND end with ')'
if(title[0][len(title[0])-1] == ")"):
    #index from the 2nd element to the 2nd to last element
    player2Char = title[0][1:len(title[0])-1]
    player2Col = "Neutral"
    #remove only the one element
    title.remove(title[0])
#if color if provided, then the second element will end with ')'
elif(title[1][len(title[1])-1] == ")"):
    player2Col = title[0][1:]
    player2Char = title[1][0:len(title[1])-1]
    #remove two elements for color and char
    title.remove(title[0])
    title.remove(title[0])
else:
    print("ERROR: invalid input")


#Now, the only thing that should be left in the list is the round
#the only acceptable round that is one word is pools
exactRoundName = ""
roundName = ""
if(title[0] == "Pools"):
    roundName = title[0]
    exactRoundName = title[0]
elif(len(title) >= 3):
    #if the length of the round name is 3 or greater, then it must be an exact round number
    #save the exact round name in variable for later use
    #save roundName as Winners Side or Losers Side for thumbnail
    firstWord = title[0].replace("'", "") 
    if(firstWord == "Winners"):
        roundName = "Winners Side"
    elif(firstWord == "Losers"):
        roundName = "Losers Side"
    else:
        for i in range(0, len(title)):
            exactRoundName += exactRoundName + title[i]
        exactRoundName = exactRoundName.replace("'", "")
else:
    #If the round is two words,
    #we need to go through each string and take out apostrophes
    roundName = title[0].replace("'", "")
    roundName += " " + title[1].replace("'", "")
    exactRoundName = roundName

#Lastly, we need to reconstruct the title to label the youtube video
#Colors of Characters will NOT be included

titleOutput = ""
if(player1Char == player2Char):
    titleOutput = tournamentName + " - " + player1Tag + " (" + player1Col + " " + player1Char + ") vs " + \
    player2Tag + " (" + player2Col + " " + player2Char + ") " + roundName
else:
    titleOutput = tournamentName + " - " + player1Tag + " (" + player1Char + ") vs " + \
    player2Tag + " (" + player2Char + ") " + roundName

title = titleOutput
print("Tournament Name: " + tournamentName)
print("Player 1 Tag: " + player1Tag)
print("Player 1 Character: " + player1Col + " " + player1Char)
print("Player 2 Tag: " + player2Tag)
print("Player 2 Character: " + player2Col + " " + player2Char)
print("Round: " + roundName)
print("Reconstructed Title: " + title)