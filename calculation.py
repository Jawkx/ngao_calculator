from itertools import permutations 

#variables for cvt2raw()
index_num2shape = [ 0 , 1 , 2 , 3 , 'Diamond' , 'Cotton' , 'Heart' , 'Spade']
index_num2picture = [ 1 , 2 , 3 , 'J' , 'Q' , 'K' ]

#General function
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
	elif arr[3][0] == arr[4][0] and arr[3][2] == 0 and arr[4][2] == 0:
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

def cvt2raw(arr):
	converted = []
	for i in range ( 0 , len(arr) ):
		current_list = arr[i]
		current_string = ''
		if len(current_list) == 3 :
			shape_index = index_num2shape.index( current_list[1] ) + 4 
			if current_list[2] == 0:
				current_string = str(current_list[0]) + ' ' + index_num2shape[shape_index]
			else:
				picture_index = index_num2picture.index( current_list[2] ) + 3
				current_string = index_num2picture[picture_index] + ' ' + index_num2shape[shape_index]

		converted.append(current_string)

	return converted

class ngaocards:
	value = None
	cardlist = [ [0,0,0] , [0,0,0] , [0,0,0] , [0,0,0] , [0,0,0] ]
	have_passport = []
	all_arrange = []

	def encodecard(self):
		if len(self.raw_cards_list) == 5 :
			for i in range ( 0 , 5 ):
				
				if len( self.raw_cards_list[i] ) == 2 :

					try:
						cardnum = int(self.raw_cards_list[i][0])
						if cardnum == 0 :
							self.cardlist[i][0] = 10
						else :
							self.cardlist[i][0] = cardnum
					except:
						if self.raw_cards_list[i][0] == 'j':
							self.cardlist[i] = [10,0,1]
						elif self.raw_cards_list[i][0] == 'q':
							self.cardlist[i] = [10,0,2]
						elif self.raw_cards_list[i][0] == 'k':
							self.cardlist[i] = [10,0,3]
						else:
							print ("invalid input : cards have unexpected attributes for type")
							print ('not and integer of not j q and k')
							break

					card_shape = self.raw_cards_list[i][1] 
					if card_shape == 'd' :
						self.cardlist[i][1] = 0
					elif card_shape == 'c' :
						self.cardlist[i][1] = 1
					elif card_shape == 'h' :
						self.cardlist[i][1] = 2
					elif card_shape == 's' :
						self.cardlist[i][1] = 3
					else:
						print ('invalid input : card have unexpected attributes for shapes')
						print ('d - diamond')
						print ('c - cotton')
						print ('h - heart')
						print ('s - spade')
						break
				else:
					print ('to much argument for a card')
					print ('REMINDER 10 SHOULD BE 0')
		else :
			print ('card is not enough')

	def printPassport(self):
		for i in range ( 0 , len( self.have_passport ) ):
			print (cvt2raw(self.have_passport[i]))

		print ('-- End of List --')

	def printAllArrange(self):
		for i in range ( 0 , len( self.all_arrange ) ):
			print (cvt2raw(self.all_arrange[i]))

		print ('-- End of List --')

	def calculate(self):
			possibility = list(permutations(self.cardlist,5))
			self.all_arrange = possibility
			for j in range ( 0 , len(possibility) ):
				if passportcheck(possibility[j]) == True :
					self.have_passport.append(possibility[j])


			if len(self.have_passport) != 0 :
				highestcount = 0
				highestcountloc = 0
				for k in range ( 0 , len(self.have_passport) ):
					current_set = self.have_passport[k]
					if fullpicturecheck( current_set ) == True:
						self.value = 'full picture'
						self.highestset = current_set
						break
					elif donggucheck( current_set ) == True :
						self.value = 'donggu'
						self.highestset = current_set
						break
					elif bouboucheck( current_set ) == True :
						self.value = 'bou bou'
						self.highestset = current_set
						break
					else :
						currentcount = countcheck( current_set )
						if currentcount > highestcount :
							highestcount = currentcount
							highestcountloc = k

						if highestcount == 0 :
							self.value = 10
						else:
							self.value = highestcount

						self.highestset = cvt2raw(self.have_passport[highestcountloc])
						
			else:
				self.value = 'mou din'

	def __init__(self,cards_input):
		self.raw_cards_list = str.split(cards_input)
		self.encodecard()
		self.calculate()

jawcard = ngaocards('3d js kd 1s 6c')
print (jawcard.value)

