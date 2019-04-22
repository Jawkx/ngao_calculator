from itertools import permutations 




def lsum(arr):
	sum = 0
	for x in range (0,len(arr)):
		sum = sum + arr[x]
		
	return sum


def passportcheck(target):
	tscount = 0
	numlist = []
	for	i in range (0,3):
		currentcount = target[i][0]

		if currentcount == 6 or currentcount == 3 :
			tscount = tscount + 1
			numlist.append(3)
		else:
			numlist.append(currentcount)

	currentsum = lsum(numlist)

	if currentsum%10 == 0 :
		return True

	for j in range (0,tscount):
		currentsum = currentsum +3

		if currentsum%10 == 0 :
			return True

	return False

def fullpicturecheck(arr):
	picturecount = 0
	for i in range (0,5):
		if arr[i][2] != 0:
			picturecount += 1

	if picturecount == 5:
		return True
	else:
		return False

def donggucheck(arr):
	if arr[3][0] == 1 and arr[3][1] == 3 and arr[4][2] != 0:
		return True
	else:
		return False

def bouboucheck(arr):
	if arr[3][2] != 0 and arr[3][2] == arr[4][2]:
		return True
	elif arr[3][0] == arr[4][0]:
		return True
	elif arr[3][0] == 3 and arr[4][0] == 6 :
		return True

	return False

def countcheck(arr):
	pos1sum = 0
	pos2sum = 0
	allpossibility = [0,0]
	fv = arr[3][0]
	sv = arr[4][0]

	if fv == 3  or fv == 6:
		allpossibility[0] = (3 + sv) % 10
		allpossibility[1] = (6 + sv) % 10
	else:
		allpossibility[0] = ( fv + sv ) % 10

	return max(allpossibility)


class cards:

	def __init__(self):
		cards_input = raw_input("input(dont need seperate) (10 is 0):")
		raw_cards_list = str.split(cards_input)
		self.cardlist = [ [0,0,0] , [0,0,0] , [0,0,0] , [0,0,0] , [0,0,0] ]

		if len(raw_cards_list) == 5 :
			for i in range ( 0 , 5 ):
				
				if len( raw_cards_list[i] ) == 2 :

					try:
						cardnum = int(raw_cards_list[i][0])
						self.cardlist[i][0] = cardnum
					except:
						if raw_cards_list[i][0] == 'j':
							self.cardlist[i] = [10,0,1]
						elif raw_cards_list[i][0] == 'q':
							self.cardlist[i] = [10,0,2]
						elif raw_cards_list[i][0] == 'k':
							self.cardlist[i] = [10,0,3]
						else:
							print 'invalid input b'
							exit()

					card_shape = raw_cards_list[i][1] 
					if card_shape == 'd' :
						self.cardlist[i][1] = 0
					elif card_shape == 'c' :
						self.cardlist[i][1] = 1
					elif card_shape == 'h' :
						self.cardlist[i][1] = 2
					elif card_shape == 's' :
						self.cardlist[i][1] = 3
				else:
					print 'invalid input a'
					exit()
		else :
			print 'card is not enough'

	def calculate(self):
			possibility = list(permutations(self.cardlist,5))
			all_arrange = []
			have_passport = []
			for j in range ( 0 , len(possibility) ):
				all_arrange.append(possibility[j])
				if passportcheck(possibility[j]) == True :
					have_passport.append(possibility[j])


			if len(have_passport) != 0 :
				highestcount = 0
				highestcountloc = 0
				for k in range ( 0 , len(have_passport) ):
					current_set = have_passport[k]
					if fullpicturecheck( current_set ) == True:
						print current_set , 'full picture'
						exit()
					elif donggucheck( current_set ) == True :
						print current_set , 'donggu'
						exit()
					elif bouboucheck( current_set ) == True :
						print current_set , 'bou bou'
						exit()
					else :
						currentcount = countcheck( current_set )
						if currentcount > highestcount :
							highestcount = currentcount
							highestcountloc = k

				print have_passport[highestcountloc] , highestcount
						
			else:
				print 'no passport'

card1 = cards()
card1.calculate()