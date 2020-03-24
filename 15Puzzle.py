#13518016
#Indra Febrio Nugroho
#24 Maret 2020
#15-Puzzle

class Matrix:
	m = []

	def printMatrix(self):
	for i in range(4):
		for j in range(4):
			print(self.m[i][j], end = " ")
		print()

	def findBlankTile(self) :
		x = -1
		y = -1

		for i in range(4):
			for j in range(4):
				if (self.m[i][j] == 16):
					x = i
					y = j
					break

			if (x != -1 and y != -1):
				break

		return x,y

	def isIdxValid(self,x,y) :
		return (x>=0 and x<4 and y>=0 and y<4)


class Node:
	parent = None
	matrix
	xBlank
	yBlank
	cost
	level = 0
	misplacedTiles

	def __init__(self, m, x, y):
		self.matrix = m
		self.xBlank = x
		self.yBlank = y

	def kurangFunc(self, x, y) :
		a = x
		b = y
		kurang=0

		for j in range(b+1,4) :
			if (self.matrix.m[a][j] < self.matrix.m[x][y]):
				kurang += 1

		for i in range(a+1,4):
			for j in range(4):
				if (self.matrix.m[i][j] < self.matrix.m[x][y]):
					kurang += 1

		return kurang

	def xFunc(self) :
		if ((self.xBlank + self.yBlank) % 2 == 0) :
			return 0
		else :
			return 1

	def isReachable(self) :
		kurang = 0
		x = 0

		for i in range(4):
			for j in range(4):
				kurang += self.kurangFunc(i,j)

		x = self.xFunc()

		return (kurang + x) % 2 == 0

	def countMisplacedTiles(self, mGoal):
		count = 0
		for i in range(4):
			for j in range(4):
				if (self.matrix.m[i][j] != mGoal[i][j] and self.matrix.m[i][j] != 16):
					count += 1
		
		self.misplacedTiles = count

	def calcCost(self, mGoal):
		self.countMisplacedTiles(mGoal)
		self.cost = self.level + self.misplacedTiles

