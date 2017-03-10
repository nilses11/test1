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
	p = "r=" + str(r) + " t=" + str(t) + " i=" + str(i)
	print p


def buy(amount):
	global r, t
	if amount <= r:
		r-=amount
		t+=amount
		print "Confirmed t+="+str(amount)

def invest(amount):
	global r, i
	if amount <= r:
		r-=amount
		i+=amount
		print "Confirmed i+="+str(amount)

def next():
	global counter, r
	counter+=1
	p = "round " + str(counter)
	print p
	r+=i


p = "round " + str(counter)
while loopvar != Q:
	loopvar = input()
