#! python3

#13518016
#Indra Febrio Nugroho
#25 Maret 2020
#15-Puzzle

import copy
import time

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
                if self.queue[i][0] < self.queue[min][0]: 
                    min = i
            item = self.queue[min] 
            del self.queue[min] 
            return item 
        except IndexError: 
            print() 
            exit()

nPuzzle = 4

def findBlankTile(m) :
	x = -1
	y = -1

	for i in range(nPuzzle):
		for j in range(nPuzzle):
			if (m[i][j] == 16):
				x = i
				y = j
				break

		if (x != -1 and y != -1):
			break

	return (x,y)

def swapTiles(m, xInit, yInit, xNew, yNew):
	temp = m[xNew][yNew]
	m[xNew][yNew] = m[xInit][yInit]
	m[xInit][yInit] = temp

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
			if (m[i][j] < 10):
				print("  ", m[i][j], end="")
			elif (m[i][j] >= 10 and m[i][j] != 16):
				print(" ", m[i][j], end="")
			else:
				print("    ", end="")
		print()
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
	for i in arr:
		if (i == m):
			found = True
			break
	return found
	
def solvePuzzle(mInit, mGoal, x, y):
	#make PrioQueue
	simpul = 0
	prioQ = PriorityQueue()
	cost = calcCost(0, mInit, mGoal) #level 0, in root, to Goal
	mGInit = []
	mGInit.append(copy.deepcopy(mInit))
	prioQ.insert((cost, 0, mInit, mGInit))

	start_time = time.time()
	isSolved = isPuzzleSolved(mInit, mGoal)
	if (isSolved):
		finish_time = time.time()
		printPath(mGenerated)
		print("Execution time: %s seconds" % (round(finish_time - start_time, 4)))
		print("Generated nodes: ", simpul)

	while (not prioQ.isEmpty() and not isSolved):
		minPuzzle = prioQ.delete()
		(oldX,oldY) = findBlankTile(minPuzzle[2])
		
		#create a child node and calculate its cost 
		for i in range(4):
			child = copy.deepcopy(minPuzzle[2])
			enter = False
			if (i==0 and isMoveValid(oldX - 1, oldY)) : 
				moveUp(child, oldX, oldY)
				enter = True
			elif (i==1 and isMoveValid(oldX + 1, oldY)) : 
				moveDown(child, oldX, oldY)
				enter = True
			elif (i==2 and isMoveValid(oldX, oldY-1)) : 
				moveLeft(child, oldX, oldY)
				enter = True
			elif (i==3 and isMoveValid(oldX, oldY+1)) : 
				moveRight(child, oldX, oldY)
				enter = True

			if (enter):
				if (not searchMatrix(minPuzzle[3], child)):
					simpul += 1
					childCost = calcCost(minPuzzle[1]+1, child, mGoal)
					mGenerated = copy.deepcopy(minPuzzle[3])
					mGenerated.append(copy.deepcopy(child))
					if (isPuzzleSolved(child, mGoal)):
						finish_time = time.time()
						printPath(mGenerated)
						print("Execution time: %s seconds" % (round(finish_time - start_time, 4)))
						print("Generated nodes: ", simpul)
						isSolved = True
						break
					else:
						prioQ.insert((childCost, minPuzzle[1]+1, copy.deepcopy(child), copy.deepcopy(mGenerated)))
				
def main() :
    fileName = input("Input filename: ")

    with open(fileName, "r") as f:
    	initial = [[int(num) for num in line.split(' ')] for line in f]
    
    (x,y) = findBlankTile(initial)
    final = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print("Initial Matrix")
    printMatrix(initial)
    print("Kurang(i) function: ", kurangFunc(initial))
    print("Kurang(i) + X function: ", kurangFunc(initial) + xFunc(x,y))

    if (isReachable(initial, x, y)):
    	print()
    	print("Path of Matrices to solve the puzzle")
    	solvePuzzle(initial,final,x,y)
    else:
    	print("Puzzle cannot be solved")

main()