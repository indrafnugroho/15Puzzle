#! python3

#13518016
#Indra Febrio Nugroho
#25 Maret 2020
#15-Puzzle

import heapq
import copy

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            min = 0
            for i in range(len(self.queue)): 
                if self.queue[i] < self.queue[min]: 
                    min = i 
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError: 
            print() 
            exit()

nPuzzle = 4

def initMatrix():
	m = []
	for i in range(4):
		m.append([])
		for j in range(4):
			m[i].append(0)
	return m

def copyMatrix(mI, mG):
	for i in range(4):
		for j in range(4):
			mG[i][j] = mI[i][j]

def findBlankTile(m) :
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

def swapTiles(m, xInit, yInit, xNew, yNew):
	temp = m[xNew][yNew]
	# print(temp)
	m[xNew][yNew] = m[xInit][yInit]
	# print(m[xNew][yNew])
	m[xInit][yInit] = temp
	# print(m[xInit][yInit])

def kurangFunc(m) :
	kurang = 0
	arrKurang = []

	for i in range(nPuzzle):
		for j in range(nPuzzle):
			arrKurang.append(m[i][j])

	for i in range(15):
		for j in range(i+1,16):
			if (arrKurang[i] > arrKurang[j]):
				kurang += 1
		
	return kurang

def xFunc(x, y) :
	if ((x + y) % 2 == 0) :
		return 0
	else :
		return 1

def isReachable(m, x, y) :
	return (kurangFunc(m) + xFunc(x,y)) % 2 == 0

def countMisplacedTiles(mInit, mGoal):
	count = 0
	for i in range(nPuzzle):
		for j in range(nPuzzle):
			if ((mInit[i][j] != 16) and (mInit[i][j] != mGoal[i][j])):
				count += 1
		
	return count

def isPuzzleSolved(mI, mG):
	return countMisplacedTiles(mI,mG) == 0

def calcCost(l, mInit, mGoal):
	return countMisplacedTiles(mInit,mGoal) + l

def printMatrix(m):
	for i in range(nPuzzle):
		for j in range(nPuzzle):
			if (m[i][j] == 16):
				print(" ", end = " ")
			else:
				print(m[i][j], end = " ")
		print()

def printPath(mGenerated) :
	for i in range(len(mGenerated)):
		printMatrix(mGenerated[i])

def isMoveValid(x,y) :
	return (x >= 0 and x < nPuzzle and y >= 0 and y < nPuzzle)

def moveUp(m,x,y) :
	swapTiles(m,x,y,x-1,y)

def moveDown(m,x,y) :
	swapTiles(m,x,y,x+1,y)

def moveLeft(m,x,y) :
	swapTiles(m,x,y,x,y-1)

def moveRight(m,x,y) :
	swapTiles(m,x,y,x,y+1)

def searchMatrix(arr,m) :
	found = False
	for i in range(len(arr)):
		if (isMatrixSame(arr[i],m)):
			found = True
			break
	return found
			
def isMatrixSame(m1,m2):
	same = True
	for i in range(4):
		for j in range(4):
			if (m1[i][j] != m2[i][j]) :
				same = False
	return same

def setXY(move,x,y):
	if (move == 1):
		x -= 1
	elif (move == 2):
		x += 1
	elif (move == 3):
		y -= 1
	elif (move == 4):
		y += 1
	elif(move == 5):
		return
def solvePuzzle(mInit, mGoal, x, y):
	#make array of generated
	mGenerated = []
	#make array of move
	mMove = []

	#make PrioQueue
	prioQ = []
	root = mInit
	level = 0
	cost = calcCost(level, root, mGoal)
	heapq.heappush(prioQ, (cost, 5, root))

	oldX = x
	oldY = y
	while (len(prioQ) != 0):
		minPuzzle = heapq.heappop(prioQ)
		print(minPuzzle)
		setXY(minPuzzle[1],oldX,oldY)
		mGenerated.append(minPuzzle[2])
		print("ini yang di pop ", minPuzzle[2])
		print("ini X nya ", oldX)
		print("ini Y nya ", oldY)
		
		# print(mGenerated[0])
		# if (isPuzzleSolved(minPuzzle,mGoal)):
		# 	printPath(mGenerated)
		# 	break
		# else :
		
		level += 1
		print("ini level ", level)
		child = initMatrix()
		#move up
		if (isMoveValid(oldX - 1, oldY)) : 
			#create a child node and calculate its cost 
			copyMatrix(minPuzzle[2],child)
			moveUp(child,oldX,oldY)

			childCost = calcCost(level, child, mGoal)
			print("ini move up ", child)

			if (not searchMatrix(mGenerated,child)):
				if (isPuzzleSolved(child,mGoal)):
					mGenerated.append(child)
					mMove.append("u")
					printPath(mGenerated)
				else:
					heapq.heappush(prioQ, (childCost,1,child))
					print("ini cost nya:", childCost)
					print("ini old nya:",oldX-1,oldY)
			
		#move down
		if (isMoveValid(oldX + 1, oldY)) : 
			#create a child node and calculate its cost 
			copyMatrix(minPuzzle[2],child)
			moveDown(child,oldX,oldY)

			childCost = calcCost(level, child, mGoal)
			print("ini move down ", child)

			if (not searchMatrix(mGenerated,child)):
				if (isPuzzleSolved(child,mGoal)):
					mGenerated.append(child)
					mMove.append("d")
					printPath(mGenerated)
					break
				else:
					heapq.heappush(prioQ, (childCost,2,child))
					print("ini cost nya:", childCost)
					print("ini old nya:",oldX+1,oldY)

		#move left
		if (isMoveValid(oldX, oldY-1)) : 
			#create a child node and calculate its cost 
			copyMatrix(minPuzzle[2],child)
			moveLeft(child,oldX,oldY)

			childCost = calcCost(level, child, mGoal)
			print("ini move left ", child)

			if (not searchMatrix(mGenerated,child)):
				if (isPuzzleSolved(child,mGoal)):
					mGenerated.append(child)
					mMove.append("l")
					printPath(mGenerated)
					break
				else:
					heapq.heappush(prioQ, (childCost,3,child))
					print("ini cost nya:", childCost)
					print("ini old nya:",oldX,oldY-1)

		#move right
		if (isMoveValid(oldX, oldY+1)) : 
			#create a child node and calculate its cost 
			copyMatrix(minPuzzle[2],child)
			moveRight(child,oldX,oldY)

			childCost = calcCost(level, child, mGoal)
			print("ini move right ", child)

			if (not searchMatrix(mGenerated,child)):
				if (isPuzzleSolved(child,mGoal)):
					mGenerated.append(child)
					mMove.append("r")
					printPath(mGenerated)
					break
				else:
					heapq.heappush(prioQ, (childCost,4,child))
					print("ini cost nya:", childCost)
					print("ini old nya:",oldX,oldY+1)
				
def main() :
    print("coba")
    initial = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 16, 12], [13, 14, 11, 15]]
    x = 2
    y = 2

    final = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print("coba2")
    if (isReachable(initial, x, y)):
    	print("coba3")
    	solvePuzzle(initial,final,x,y)
    	print("coba4")
    else:
    	print("Raiso")

main()