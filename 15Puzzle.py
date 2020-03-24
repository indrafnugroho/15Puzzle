#13518016
#Indra Febrio Nugroho
#24 Maret 2020
#15-Puzzle

def isIdxValid(x,y) :
	return (x>=0 and x<4 and y>=0 and y<4)

def kurangFunc(m, x, y) :
	a = x
	b = y
	kurang=0

	for j in range(b+1,4) :
		if (m[a][j] < m[x][y]):
			kurang += 1

	for i in range(a+1,4):
		for j in range(4):
			if (m[i][j] < m[x][y]):
				kurang += 1

	return kurang

def xFunc(x,y) :
	if ((x + y) % 2 == 0) :
		return 0
	else :
		return 1

def isReachable(m, xBlank, yBlank) :
	kurang = 0
	x = 0

	for i in range(4):
		for j in range(4):
			kurang += kurangFunc(m,i,j)

	x = xFunc(xBlank,yBlank)

	return (kurang + x) % 2 == 0

def printMatrix(m):
	for i in range(4):
		for j in range(4):
			print(m[i][j], end = " ")
		print()

def findIdxBlank(m) :
	x = -1
	y = -1

	for i in range(4):
		for j in range(4):
			if (m[i][j] == 16):
				x = i
				y = j
				break

		if (x != -1 and y != -1):
			break

	return x,y

def main() :
	mGoal = ([1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16])

	

