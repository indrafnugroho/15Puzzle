#13518016
#Indra Febrio Nugroho
#24 Maret 2020
#15-Puzzle

class Matrix:
	m = []
	xBlank
	yBlank

	def __init__(self, m, x, y):
		self.m = m
		self.xBlank = x
		self.yBlank = y

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

	def isMoveValid(self,x,y) :
		return ((self.xBlank + x) >= 0 and (self.xBlank+x) < 4 and (self.yBlank + y) >= 0 and (self.yBlank + y) < 4)

	def swapTiles(self, xInit, yInit, xNew, yNew):
		temp = self.m[xNew][yNew]
		self.m[xNew][yNew] = self.m[xInit][yInit]
		self.m[xInit][yInit] = temp


class PuzzleNode:
	parent
	matrix
	cost
	level
	misplacedTiles

	def __init__(self, p, m, l):
		self.parent = p
		self.matrix = m
		self.level = l

	def kurangFunc(self, x, y) :
		a = x
		b = y
		kurang=0

		for i in range(a,4):
			if (i==a) :
				for j in range(b+1,4) :
					if (self.matrix.m[a][j] < self.matrix.m[x][y]):
						kurang += 1
			else:
				for j in range(4):
					if (self.matrix.m[i][j] < self.matrix.m[x][y]):
						kurang += 1
		
		return kurang

	def xFunc(self) :
		if ((self.matrix.xBlank + self.matrix.yBlank) % 2 == 0) :
			return 0
		else :
			return 1


	def isReachable(self) :
		kurang = 0

		for i in range(4):
			for j in range(4):
				kurang += self.kurangFunc(i,j)

		return (kurang + self.xFunc()) % 2 == 0

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

	def printPath(self) :
		if (self.parent is None):
			#do nothing
		else:
			printPath(self.parent)
			self.matrix.printMatrix()

			print()

	def solvePuzze(self, pq, mGoal):
		#push this node to prioqueue

		while (!pq.isEmpty()):
			min = pq.top()

			pq.pop()

			if (min.misplacedTiles == 0):
				min.matrix.printPath()
				break
			else :
				for i in range(4):
					


'''
        // do for each child of min 
        // max 4 children for a node 
        for (int i = 0; i < 4; i++) 
        { 
            if (isSafe(min->x + row[i], min->y + col[i])) 
            { 
                // create a child node and calculate 
                // its cost 
                Node* child = newNode(min->mat, min->x, 
                              min->y, min->x + row[i], 
                              min->y + col[i], 
                              min->level + 1, min); 
                child->cost = calculateCost(child->mat, final); 
  
                // Add child to list of live nodes 
                pq.push(child); 
            } 
        } 
    } 


    // Create a priority queue to store live nodes of 
    // search tree; 
    priority_queue<Node*, std::vector<Node*>, comp> pq; 
  
    // create a root node and calculate its cost 
    Node* root = newNode(initial, x, y, x, y, 0, NULL); 
    root->cost = calculateCost(initial, final); 
  
    // Add root to list of live nodes; 
    pq.push(root); 
  
    // Finds a live node with least cost, 
    // add its childrens to list of live nodes and 
    // finally deletes it from the list. 
    
} 
'''
