#13518016
#Indra Febrio Nugroho
#24 Maret 2020
#15-Puzzle

import heapq

class Node:
	def __init__(self, m, x, y, newX, newY, l, p):
		self.parent = p
		self.matrix = self.swapTiles(m,x,y,newX,newY)
		self.cost = 1000000 #infinite val
		self.misplacedTiles = 1000000
		self.level = l
		self.xBlank = newX
		self.yBlank = newY

	# def __lt__(self, other):
	# 	return self.cost < other.cost

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

	def swapTiles(self, m, xInit, yInit, xNew, yNew):
		mTemp = m

		temp = mTemp[xNew][yNew]
		mTemp[xNew][yNew] = mTemp[xInit][yInit]
		mTemp[xInit][yInit] = temp

		return mTemp

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
			self.printPath(n.parent)
			self.printMatrix(n.matrix)
			print()

	def isMoveValid(self,x,y) :
		return (x >= 0 and x < self.n and y >= 0 and y < self.n)

	def solvePuzzle(self, mInit, mGoal, x, y):
		#make PrioQueue
		prioQ = []
		root = Node(mInit, x, y, x, y, 0, None)
		root.misplacedTiles = self.countMisplacedTiles(mInit,mGoal)
		root.cost = self.calcCost(root.level, mInit, mGoal)
		heapq.heappush(prioQ, root)

		while (len(prioQ) != 0):
			min = heapq.heappop(prioQ)
			if (min.misplacedTiles == 0):
				self.printPath(min)
				break
			else :
				for i in range(self.n):
					newXBlank = min.xBlank + self.row[i]
					newYBlank = min.yBlank + self.col[i]

					if (self.isMoveValid(newXBlank,newYBlank)) : 
                	
                		#create a child node and calculate its cost 
						child = Node(min.matrix, min.xBlank, min.yBlank, newXBlank, newYBlank, min.level + 1, min) 
						child.misplacedTiles = self.countMisplacedTiles(child.matrix,mGoal)
						child.cost = self.calcCost(child.level, child.matrix,mGoal) 
  	
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

def testing():
	initial = [[1, 2, 3, 4], [5, 6, 16, 8], [9, 10, 7, 11], [13, 14, 15, 12]]
	xBlank = 1
	yBlank = 2

	final = ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16])

	puzzle = PuzzleNode()
	# root = Node(initial, xBlank, yBlank, xBlank, yBlank, 0, None)
	# root.misplacedTiles = puzzle.countMisplacedTiles(initial,final)
	# root.cost = puzzle.calcCost(root.level, initial, final)
	# print(root.cost)
	# print(puzzle.countMisplacedTiles(initial,final))

	prioQ = []
	root = Node(initial, xBlank, yBlank, xBlank, yBlank, 0, None)
	root.misplacedTiles = puzzle.countMisplacedTiles(initial,final)
	root.cost = puzzle.calcCost(root.level, initial, final)
	heapq.heappush(prioQ, (root.cost,root))

	# min = heapq.heappop(prioQ)

	# print(len(prioQ))

	while (len(prioQ) != 0):
		min = heapq.heappop(prioQ)
		if (min[1].misplacedTiles == 0):
			puzzle.printPath(min[1])
			# print("disini1")
			break
		else :
			# print("disini2")
			for i in range(puzzle.n):
				newXBlank = min[1].xBlank + puzzle.row[i]
				# print(min.xBlank, newXBlank)
				newYBlank = min[1].yBlank + puzzle.col[i]
				# print(min.yBlank, newYBlank)

				if (puzzle.isMoveValid(newXBlank,newYBlank)) : 
					# print("disini3")
               		#create a child node and calculate its cost 
					child = Node(min[1].matrix, min[1].xBlank, min[1].yBlank, newXBlank, newYBlank, min[1].level + 1, min[1]) 
					# print(child.xBlank)
					# print(child.yBlank)
					# print(child.matrix)
					# print(child.level)
					child.misplacedTiles = puzzle.countMisplacedTiles(child.matrix,final)
					child.cost = puzzle.calcCost(child.level, child.matrix,final)
					# print(child.misplacedTiles)
					# print(child.cost)
  					
 #               	#Add child to list of live nodes 
					heapq.heappush(prioQ, (child.cost,child))
					print(child.matrix)

testing()