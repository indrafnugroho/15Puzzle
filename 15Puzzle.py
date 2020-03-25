#13518016
#Indra Febrio Nugroho
#24 Maret 2020
#15-Puzzle

import heapq

class Node:
	def __init__(self, m, x, y, newX, newY, l, p):
		self.setParent(p)
		self.setMatrix(m)
		self.setCost(1000000) #infinite val
		self.setMisplacedTiles(1000000)
		self.setLevel(l)
		self.setXBlank(newX)
		self.setYBlank(newY)
		self.swapTiles(x,y,newX,newY)

	def setParent(self,p):
		self._parent = p
	def setMatrix(self,m):
		self._matrix = m
	def setCost(self,c):
		self._cost = c
	def setMisplacedTiles(self,mt):
		self._misplacedTiles = mt
	def setLevel(self,l):
		self._level = l
	def setXBlank(self,x):
		self._xBlank = x
	def setYBlank(self,y):
		self._yBlank = y

	def getParent(self):
		return self._parent
	def getMatrix(self):
		return self._matrix
	def getCost(self):
		return self._cost
	def getMisplacedTiles(self):
		return self._misplacedTiles
	def getLevel(self):
		return self._level
	def getXBlank(self):
		return self._xBlank
	def getYBlank(self):
		return self._yBlank

	def __lt__(self, other):
		return self.getCost() < other.getCost()

	def findBlankTile(self, m) :
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

	def swapTiles(self, xInit, yInit, xNew, yNew):
		mTemp = self.getMatrix()
		temp = mTemp[xNew][yNew]
		mTemp[xNew][yNew] = mTemp[xInit][yInit]
		mTemp[xInit][yInit] = temp
		self.setMatrix(mTemp)

class PuzzleNode:
	n = 4
	row = [1,0,-1,0]
	col = [0,-1,0,1]

	def kurangFunc(self, m) :
		kurang = 0
		arrKurang = []

		for i in range(self.n):
			for j in range(self.n):
				arrKurang.append(m[i][j])

		print(arrKurang)

		for i in range(15):
			for j in range(i+1,16):
				if (arrKurang[i] > arrKurang[j]):
					kurang += 1
		
		return kurang

	def xFunc(self, x, y) :
		if ((x + y) % 2 == 0) :
			return 0
		else :
			return 1

	def isReachable(self, m, x, y) :
		return (self.kurangFunc(m) + self.xFunc(x,y)) % 2 == 0

	def countMisplacedTiles(self, mInit, mGoal):
		count = 0
		for i in range(self.n):
			for j in range(self.n):
				if ((mInit[i][j] != 16) and (mInit[i][j] != mGoal[i][j])):
					count += 1
		
		return count

	def calcCost(self, l, mInit, mGoal):
		return self.countMisplacedTiles(mInit,mGoal) + l

	def printMatrix(self, m):
		for i in range(self.n):
			for j in range(self.n):
				print(m[i][j], end = " ")
			print()

	def printPath(self, n) :
		if (n is None):
			return
		else:
			self.printPath(n.getParent())
			self.printMatrix(n.getMatrix())
			print()

	def isMoveValid(self,x,y) :
		return (x >= 0 and x < self.n and y >= 0 and y < self.n)

	def solvePuzzle(self, mInit, mGoal, x, y):
		#make PrioQueue
		prioQ = []
		root = Node(mInit, x, y, x, y, 0, None)
		root.setMisplacedTiles(self.countMisplacedTiles(mInit,mGoal))
		root.setCost(self.calcCost(root.getLevel(), mInit, mGoal))
		heapq.heappush(prioQ, root)

		while (len(prioQ) != 0):
			minPuzzle = heapq.heappop(prioQ)
			if (minPuzzle.getMisplacedTiles() == 0):
				self.printPath(minPuzzle)
				break
			else :
				for i in range(self.n):
					newXBlank = minPuzzle.getXBlank() + self.row[i]
					newYBlank = minPuzzle.getYBlank() + self.col[i]

					if (self.isMoveValid(newXBlank,newYBlank)) : 
                	
                		#create a child node and calculate its cost 
						child = Node(minPuzzle.getMatrix(), minPuzzle.getXBlank(), minPuzzle.getYBlank(), newXBlank, newYBlank, minPuzzle.getLevel + 1, minPuzzle) 
						child.setMisplacedTiles(self.countMisplacedTiles(child.matrix,mGoal))
						child.setCost(self.calcCost(child.level, child.matrix,mGoal))
  	
                		#Add child to list of live nodes 
						heapq.heappush(prioQ, child)


def main() :
    initial = ([16, 2, 3, 4], [1, 6, 7, 8], [5, 10, 11, 12], [9, 13, 14, 15])
    xBlank = 1
    yBlank = 2

    final = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16])

    puzzle = PuzzleNode()
    

    if (puzzle.isReachable(initial, xBlank, yBlank)):
    	puzzle.solvePuzzle(initial,final,xBlank,yBlank)
    else:
    	print("Raiso")