#STATIC
Q, q = -1, -1
loopvar = ""

#CHANGEABLES
r = 1000
t = 0
i = 100
counter = 1

#FUNCTIONS
def status():
	return "r=" + str(r) + " t=" + str(t) + " i=" + str(i)

def buy(amount):
	global r, t
	if amount <= r:
		r-=amount
		t+=amount
		return "Confirmed t+="+str(amount)

def invest(amount):
	global r, i
	if amount <= r:
		r-=amount
		i+=amount
		return "Confirmed i+="+str(amount)

def next():
	global counter, r
	counter+=1
	r+=i
	return "round " + str(counter)


print "round " + str(counter)
while loopvar != Q:
	loopvar = input()
	print str(loopvar)

	
	
	""""
	from random import randint

#aiModes = ["AGR","DEF","BAL","SMA"]
#aiMode = aiModes[randint(0,3)]

#CHANGEABLES
air = 1000
ait = 0
aii = 100

def runAi():
	#global aiMode # impl agr først
	buy(1000)
	attack(500)
	"""