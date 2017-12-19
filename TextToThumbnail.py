from PIL import Image, ImageFont, ImageDraw
import PIL, random, sys, os, numpy

class Thumbnail(object):
	def __init__(self, ):
		global textfile
		global fontType
		textfile = "input.txt"
		fontType = "Times New Roman.ttf"
	
	#This function takes in the input textfile and gets all the variables that we can get from it
	def stringParse(self):
		global title
		global tournamentName
		global tournamentNumber
		global player1Tag
		global player2Tag
		global player1Char
		global player2Char
		global player1Col
		global player2Col
		global exactRoundName
		global roundName
		#read in the title 
		str1 = open("input.txt", 'r+').read()

		#split the title separated by white space 
		#save as a LIST named title 
		title = str1.split()

		#first, we need to find the index of the dash,
		#so that everything before it as the tournament name 
		indexDash = 0
		for i in range(0, len(title)):    
			#it is important that the dash is separated by WHITESPACE or this code will not work
			if(title[i] == "-"):        
				indexDash = i
				break

		#once we know the index of the dash, we know that everthing before it is the tournament name
		tournamentName = ""
		tournamentNumber = ""

		#add whitespace inbetween each word
		for i in range(0, indexDash - 1):
			tournamentName += title[i] + " "

		#find the number of the tournament, if it exists
		if(title[indexDash - 1][0].isdigit()):
			tournamentNumber = title[indexDash - 1]

		#delete the tournament name AND DASH from the title
		#we will recreate the title at the end
		for i in range(0, indexDash + 1):
			title.remove(title[0])

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
		for i in range(0, indexPar):
			title.remove(title[0])



		#now, we need a series of if statements because some characters have more than one word
		player1Char = ""
		player1Col = ""
		#if characters are two words, then the first word could be one of these five
		#it could be the first OR second word because the color could be in front
		if(title[0][1:6] == "Young" or title[0][1:4] == "Dr." or title[0][1:4] == "Ice" or 
			title[0][1:8] == "Captain" or title[0][1:7] == "Donkey" or title[1][0:5] == "Young" 
			or title[1][0:3] == "Dr." or title[1][0:3] == "Ice" or title[1][0:7] == "Captain"
			or title[1][0:6] == "Donkey"):
			#if color is not provided, then the first element in the list will begin with '('
			#and the second word will end with ')'
			if(title[1][len(title[1])-1] == ")"):
				#index the first word without the '(' and the second word without the ')' at the end
				player1Char = title[0][1:len(title[0])] + " " + title[1][0:len(title[1])-1]
				player1Col = "Neutral"
				#remove only the two elements
				for i in range(0, 2):
					title.remove(title[0])
			#if color if provided, then the third word will end with ')'
			elif(title[2][len(title[2])-1] == ")"):
				#index the first word for the color 
				#index the second and third words for the character
				player1Col = title[0][1:]
				player1Char = title[1][0:len(title[1])] + " " + title[2][0:len(title[2])-1]
				#remove three elements for color and char
				for i in range(0, 3):
					title.remove(title[0])
			else:
				print("ERROR: invalid input")
		#special case for Mr. Game and Watch because it's FOUR WORDS 		
		elif(title[0][1:4] == "Mr." or title[1][0:3] == "Mr."):
			#if color is not provided, then the fourth element in the list will end with ')'
			if(title[3][len(title[3])-1] == ")"):
				#index each word for Mr. Game and Watch
				player1Char = title[0][1:len(title[0])] + " " + title[1] + " " + \
					title[2] + " " + title[3][0:len(title[3])-1]
				player1Col = "Neutral"
				#remove only the four elements
				for i in range(0, 4):
					title.remove(title[0])
			#if color if provided, then the fifth element will end with ')'
			elif(title[4][len(title[4])-1] == ")"):
				player1Col = title[0][1:]
				player1Char = title[1][0:len(title[1])] + " " + title[2] + " " + \
					title[3] + " " + title[4][0:len(title[4])-1]
				#remove the five elements
				for i in range(0, 5):
					title.remove(title[0])
			else:
				print("ERROR: invalid input")
		#ELSE, any other character will be ONE WORD
		else:
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
				for i in range(0, 2):
					title.remove(title[0])
			else:
				print("ERROR: invalid input")

		#REMOVE the 'vs'
		title.remove(title[0])

		#Now, we do the SAME CODE, but for Player 2

		#we want to find the index of the first parenthesis, so that
		#we know how long player 2's tag is
		indexPar2 = 0
		for i in range(0, len(title)):
			if(title[i][0] == "("):     #again, it is very important that there is WHITESPACE before '('
				indexPar2 = i
				break

		#Using the index of parenthesis, write player 2's tag to the variable 
		player2Tag = ""
		for i in range(0, indexPar2-1):
			player2Tag += title[i] + " "
		player2Tag += title[indexPar2-1]

		#Delete player 2's tag from the title
		for i in range(0, indexPar2):
			title.remove(title[0])


		player2Char = ""
		player2Col = ""
		#The next series of if statements are for different character's word length 
		#IF the character is TWO words, then the first word can be the following
		if(title[0][1:6] == "Young" or title[0][1:4] == "Dr." or title[0][1:4] == "Ice" or 
			title[0][1:8] == "Captain" or title[0][1:7] == "Donkey"  or title[1][0:5] == "Young" or 
			title[1][0:3] == "Dr." or title[1][0:3] == "Ice" or title[1][0:7] == "Captain" or 
			title[1][0:6] == "Donkey"):
			#if color is not provided, then the second word will end with ')'
			if(title[1][len(title[1])-1] == ")"):
				#index the first two words for player 2's character
				player2Char = title[0][1:len(title[0])] + " " + title[1][0:len(title[1])-1]
				player2Col = "Neutral"
				#remove only the two elements for the character
				for i in range(0, 2):
					title.remove(title[0])
			#if color if provided, then the third word will end with ')'
			elif(title[2][len(title[2])-1] == ")"):
				#index the first word for character's color
				#index the second and third word for the character
				player2Col = title[0][1:]
				player2Char = title[1][0:len(title[1])] + " " + title[2][0:len(title[2])-1]
				#remove three elements for color and char
				for i in range(0, 3):
					title.remove(title[0])
			else:
				print("ERROR: invalid input")
		#Special case for Mr. Game and Watch because it's FOUR WORDS 
		elif(title[0][1:4] == "Mr." or title[1][0:3] == "Mr."):
			#if color is not provided, then the fourth element will end with ')'
			if(title[3][len(title[3])-1] == ")"):
				#index the four words for the character
				player2Char = title[0][1:len(title[0])] + " " + title[1] + " " + title[2] + \
					" " + title[3][0:len(title[3])-1]
				player2Col = "Neutral"
				#remove the four words
				for i in range(0, 4):
					title.remove(title[0])
			#if color if provided, then the fifth element will end with ')'
			elif(title[4][len(title[4])-1] == ")"):
				#index the first word for the character's color
				#index the second and third word for the character
				player2Col = title[0][1:]
				player2Char = title[1][0:len(title[1])] + " " + title[2] + " " + title[3] + \
					" " + title[4][0:len(title[4])-1]
				#remove five elements for color and char
				for i in range(0, 5):
					title.remove(title[0])
			else:
				print("ERROR: invalid input")
		#Else, any other word will mean that the character is ONE word
		else:
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
				#index the first word for the character's color
				#index the second and third word for the character
				player2Col = title[0][1:]
				player2Char = title[1][0:len(title[1])-1]
				#remove two elements for color and char
				for i in range(0, 2):
					title.remove(title[0])
			else:
				print("ERROR: invalid input")



		#we need to store two variables for the round name because a round name 
		#such as "Winner's round 7" should be kept in exact form for later use,
		#but the roundName variable should be kept as "Winners Side"
		exactRoundName = ""
		roundName = ""

		#Now, the only thing that should be left in the list is the round
		#The only acceptable round that is one word is pools
		if(title[0] == "Pools"):
			roundName = title[0]
			exactRoundName = title[0]
		#if the title size is 3 or greater, then we know it is an exact round name,
		#because all of the other round names (e.g., Winners Finals) are two words 
		elif(len(title) >= 3):
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
				#take out apostrophes
				exactRoundName = exactRoundName.replace("'", "")
		#Every other case will mean that the round name is two words
		else:
			#If the round is two words,
			#we need to go through each string and take out apostrophes
			roundName = title[0].replace("'", "")
			roundName += " " + title[1].replace("'", "")
			exactRoundName = roundName

		#Lastly, we need to reconstruct the title to label the youtube video
		#Colors of Characters will not be include, UNLESS the players' characters 
		#are the same and their colors are different 

		titleOutput = ""
		if(player1Char == player2Char and player1Col != player2Col):
			titleOutput = tournamentName + " " + tournamentNumber + " - " + player1Tag + \
			" (" + player1Col + " " + player1Char + ") vs " + \
			player2Tag + " (" + player2Col + " " + player2Char + ") " + roundName
		else:
			titleOutput = tournamentName + " " + tournamentNumber + 	" - " + \
			player1Tag + " (" + player1Char + ") vs " + \
			player2Tag + " (" + player2Char + ") " + roundName

		title = titleOutput

	def initImages(self):
		#This function just initializes all of the images that we will be manipulating

		#Declare all of the image variables that we will be using
		global top
		global mid
		global bot
		global player1Image
		global player2Image
		global versus
		global melee
		global logo

		#Set the variables to something, this assumes that all the corrent PNGs will be in the folder
		top = Image.open("TOP.png")
		bot = Image.open("BOT.png")
		mid = Image.open("MID.png")
		versus = Image.open("VERSUS.png")
		melee = Image.open("MELEE.png")
		logo = Image.open("LOGO.png")

		#NOTE: All character renders must be saved in the format of Character Color.PNG
		#The neutral color should be saved as Character Neutral.PNG
		player1Image = Image.open(player1Char+ " " + player1Col+".PNG")
		player2Image = Image.open(player2Char+ " " + player2Col+".PNG")

	#This function puts together the final BOT image. We are assuming that each portion of the bot image will
	#take up 1/3 of the width. 
	def buildBot(self):
		global logoCross
		logoCross = False

		#When putting images in the corner it can look a little jarring for them to be right on the edge. I have put in an offset from
		#the corners, you can change this to whatever looks good
		offset = 10

		#We are assuming that each part of the bottom image will take up 1/3 of it, this can be changed by changing the space allotted
		spaceForMelee = int(bot.width/3 - offset)

		#This resizes the melee.png if necessary, and then puts it in the bottom LH corner of the bot image
		#If the melee.png fits within the boundaries specified, we don't mess with it
		if(melee.height > spaceForMelee or melee.width > int(bot.height)):
			newMelee = fitImage(melee,(spaceForMelee, bot.height))
		else:
			newMelee = melee.copy()
		bot.paste(newMelee,placeBotLHCorner(newMelee, (offset,bot.height - offset)), mask=newMelee)

		#Different value for the offset of the logo from the bottom
		logoOffset = 0
		#We are assuming that the logo must fit in the middle third of BOT.png
		#You can choose how far you want the logo to go into the middle picture
		spaceForLogo = int(bot.width/3)
		extraSpaceForLogo = int(mid.height * .25)
		
		#If the logo does cross, we create a global variable for the part of the image in mid and the image in bot
		#We save logoMid for buildMid()
		if(not logoCross):
			if(logo.height > spaceForLogo or logo.width > int(bot.height)):
				newLogo = fitImage(logo,(spaceForLogo, bot.height))
			else:
				newLogo = logo.copy()
			logoStartingCol = int(bot.width/2 - int(newLogo.width/2))
			bot.paste(newLogo, (logoStartingCol,6), mask=newLogo)
		if(logoCross):
			global logoMid
			global logoBot

			newLogo = fitImage(logo,(spaceForLogo, bot.height + extraSpaceForLogo))
			logoBot = newLogo.crop((0, newLogo.height - bot.height, newLogo.width, newLogo.height))
			logoMid = newLogo.crop((0, 0, newLogo.width, newLogo.height - bot.height))
			logoStartingRow = int(bot.width/2 - int(newLogo.width/2))
			bot.paste(logoBot, placeBotLHCorner(logoBot, (logoStartingRow,bot.height - logoOffset)), mask=logoBot)


		#Font Info needs to be in the form: (Canvas, Font, Fontsize, Text)		
		fontInfo = (bot, fontType, 280,"#"+tournamentNumber)
		drawFont(fontInfo, fontCoordinatesRHBottom(fontInfo, (bot.width, bot.height)))

	def buildMid(self):
		#Assigning boundaries for the different images to be pasted in
		spaceForVersus = int(mid.width/4)
		spaceForRound = int(mid.width/4)
		#There is a split depending on whether or not the logo has crossed over
		if(not logoCross):
			#Create the VS and the round, center them, and paste them in
			newVersus = fitImage(versus,(spaceForVersus, int(mid.height*2.5/4)))
			mid.paste(newVersus, (int(mid.width/2-newVersus.width/2),10), mask=newVersus)
			startingRowRound = newVersus.height + 10
			fontInfo = (mid, fontType, 80, roundName)
			drawFont(fontInfo, fontCoordinatesCenteredTop(fontInfo,(int(mid.width/2), startingRowRound)))
			spaceForImages = int(mid.width*4/9)

			#Create and paste in the first player's character's image on the left side
			newPlayer1Image = fitImage(player1Image, (spaceForImages, mid.height))
			mid.paste(newPlayer1Image, (mid.width*2/9-newPlayer1Image.width/2,0), mask = newPlayer1Image)

			#Create and paste in the second player's character's image on the right side, flipped
			newPlayer2Image = fitImage(player2Image, (spaceForImages, mid.height))
			newPlayer2Image = newPlayer2Image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
			mid.paste(newPlayer2Image, placeTopRHCorner(newPlayer2Image,(mid.width*7/9+newPlayer2Image.width/2,0)), mask = newPlayer2Image)
		else:
			#Create the VS and the round, center them, and paste them in, but make sure to not take up the space of the logo
			newHeight = mid.height - logoMid.height
			newVersus = fitImage(versus,(spaceForVersus, int(newHeight*3/4)))
			mid.paste(newVersus, (int(mid.width/2-newVersus.width/2),10), mask=newVersus)
			startingRowRound = newVersus.height
			fontInfo = (mid, fontType, 100, roundName)
			drawFont(fontInfo, fontCoordinatesCenteredTop(fontInfo,(int(mid.width/2), startingRowRound)))
			mid.paste(logoMid, (int(mid.width/2 - logoMid.width/2),int(mid.height - logoMid.height)), mask=logoMid)
			spaceForImages = int(mid.width*4/9)

			#Create and paste in the first player's character's image on the left side
			newPlayer1Image = fitImage(player1Image, (spaceForImages, mid.height))
			mid.paste(newPlayer1Image, (mid.width*2/9-newPlayer1Image.width/2,0), mask = newPlayer1Image)

			#Create and paste in the second player's character's image on the right side, flipped
			newPlayer2Image = fitImage(player2Image, (spaceForImages, mid.height))
			newPlayer2Image = newPlayer2Image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
			mid.paste(newPlayer2Image, placeTopRHCorner(newPlayer2Image,(mid.width*7/9+newPlayer2Image.width/2,0)), mask = newPlayer2Image)

	def buildTop(self):
		#Create the font types for both player tags
		player1TagFontSize = 200
		player2TagFontSize = 200
		if(len(player1Tag) > 3):
			player1TagFontSize = 165
		if(len(player2Tag) > 3):
			player2TagFontSize = 165
		if(len(player1Tag) > 7):
			player1TagFontSize = 140
		if(len(player2Tag) > 7):
			player2TagFontSize = 140
		if(len(player1Tag) > 9):
			player1TagFontSize = 115
		if(len(player2Tag) > 9):
			player2TagFontSize = 115
		if(len(player1Tag) > 11):
			player1TagFontSize = 90
		if(len(player2Tag) > 11):
			player2TagFontSize = 90
		if(len(player1Tag) > 15):
			player1TagFontSize = 75
		if(len(player2Tag) > 15):
			player2TagFontSize = 75
		if(len(player1Tag) > 17):
			player1TagFontSize = 70
		if(len(player2Tag) > 17):
			player2TagFontSize = 70
		if(len(player1Tag) > 19):
			player1TagFontSize = 60
		if(len(player2Tag) > 19):
			player2TagFontSize = 60


		fontInfo1 = (top, fontType, player1TagFontSize, player1Tag.upper())
		fontInfo2 = (top, fontType, player2TagFontSize, player2Tag.upper())
		spaceForTags = top.width/2

		drawFont(fontInfo1, fontCoordinatesCentered(fontInfo1,(int(top.width/4), int(top.height/2))))
		drawFont(fontInfo2, fontCoordinatesCentered(fontInfo2,(int(top.width*3/4), int(top.height/2))))

	def combine(self):
		img = Image.new("RGBA", (top.width,top.height+mid.height+mid.height),(255,255,255))
		img.paste(top, (0,0))
		img.paste(mid, (0,top.height))
		img.paste(bot, (0,top.height+mid.height))
		img.show()


		



#REQUIRES: fontInfo is a 4-tuple with the given parameters: (canvas, font, fontsize, text)
#EFFECTS: Pastes an image of the text onto the canvas with the given font and fontsize
#MODIFIES: Canvas
def drawFont(fontInfo, coordinates):
	draw = ImageDraw.Draw(fontInfo[0])
	fontreal = ImageFont.truetype(fontInfo[1], fontInfo[2])
	draw.text(coordinates, fontInfo[3], font=fontreal)

#REQUIRES: fontInfo is a 4-tuple with the given parameters: (canvas, font, fontsize, text)
#HOW TO USE: Use these functions when you are trying to line up a corner of your text that is not the 
#			 top lefthand corner. Therefore, if you are trying to get font to fit into the bottom
#			 righthand corner of your canvas, just make sure to call fontCoordinatesRHBottom
#			 with the correct font info and the coordinates of the righthand corner, and it will convert
#			 it into a form that the drawFont function will be able to interpret correctly
def fontCoordinatesRHBottom(fontInfo, coordinates):
	draw = ImageDraw.Draw(fontInfo[0])
	font = ImageFont.truetype(fontInfo[1], fontInfo[2])
	return (coordinates[0] - draw.textsize(fontInfo[3], font=font)[0], coordinates[1] - draw.textsize(fontInfo[3], font=font)[1])

def fontCoordinatesRHTop(fontInfo, coordinates):
	draw = ImageDraw.Draw(fontInfo[0])
	font = ImageFont.truetype(fontInfo[1], fontInfo[2])
	return (coordinates[0] - draw.textsize(fontInfo[3], font=font)[0], coordinates[1])
	

def fontCoordinatesLHBottom(fontInfo, coordinates):
	draw = ImageDraw.Draw(fontInfo[0])
	font = ImageFont.truetype(fontInfo[1], fontInfo[2])
	return (coordinates[0], coordinates[1] - draw.textsize(fontInfo[3], font=font)[1])

def fontCoordinatesCenteredTop(fontInfo, coordinates):
	draw = ImageDraw.Draw(fontInfo[0])
	font = ImageFont.truetype(fontInfo[1], fontInfo[2])
	return (coordinates[0] - (draw.textsize(fontInfo[3], font=font)[0])/2, coordinates[1])

def fontCoordinatesCentered(fontInfo, coordinates):
	draw = ImageDraw.Draw(fontInfo[0])
	font = ImageFont.truetype(fontInfo[1], fontInfo[2])
	return (coordinates[0] - (draw.textsize(fontInfo[3], font=font)[0])/2, coordinates[1] - (draw.textsize(fontInfo[3], font=font)[1])/2)







#REQUIRES: img1 to be an image, boundarySize to be a tuple in the form (width, height)
#EFFECTS: Takes in an image and a boundary that it needs to fit in. If the image is too large 
#         or too small, it will resize the image to fit within the boundary without changing the aspect ratio
#		  It returns the resized image
#MODIFIES: img1
def fitImage(img1, boundarySize):
	aspectRatioImg = float(img1.width)/img1.height
	aspectRatioBoundary = float(boundarySize[0])/boundarySize[1]
	if(aspectRatioImg > aspectRatioBoundary):
		multiplier = float(boundarySize[0])/img1.width
		img1 = img1.resize((int(img1.width*multiplier),int(img1.height*multiplier)), PIL.Image.LANCZOS)
	else:
		multiplier = float(boundarySize[1])/img1.height
		img1 = img1.resize((int(img1.width*multiplier),int(img1.height*multiplier)), PIL.Image.LANCZOS)
	return img1

#REQUIRES: coordinates to be a tuple in the form (x,y)
#EFFECTS: These three functions allow you to plug in the coordinates of the corner specified in the title of the function
#		  and it will return the corresponding top left hand corner that you need to place the image

#		  For example, if you know that the picture you are trying to copy goes into the right hand corner of the larger image
#         simply put placeBotRHCorner(img, coordinates) where the paste function asks for coordinates, and in this case the 
#		  coordinates you input are actually the bot right hand corner, not the top right hand corner that paste usually wants
def placeTopRHCorner(img1, coordinates):
	coordinates = (coordinates[0] - img1.width, coordinates[1]);
	return coordinates
def placeBotRHCorner(img1, coordinates):
	coordinates = (coordinates[0] - img1.width, coordinates[1] - img1.height);
	return coordinates
def placeBotLHCorner(img1, coordinates):
	coordinates = (coordinates[0], coordinates[1] - img1.height);
	return coordinates





mingeeSux = Thumbnail()
mingeeSux.stringParse()
mingeeSux.initImages()
mingeeSux.buildBot()
mingeeSux.buildMid()
mingeeSux.buildTop()
mingeeSux.combine()




	






	
