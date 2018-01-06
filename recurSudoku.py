#
# Numan Khan 10/25/2015
#
from time import time
words = open('sudoku128.txt').read().split()
matrix = []
def createMatrix(num):
   char = {}
   counter = 0
   prob = words[int(num)]
   for c in range(0,len(prob),9):
      char = {}
      temp = []
      row = prob[c:(c+9)]
      for k in range(9):
         char[k] = row[k:k+1]
      key = int(c/9)
      matrix.append(char)
      if key == 8:
         return matrix

def display(matrix):
   for x in range(len(matrix)):
      temp = matrix[x]
      print(temp[0] + temp[1] + temp[2] + "|" + temp[3] + temp[4] + temp[5] + "|" + temp[6] + temp[7] + temp[8])
      if ((x+1) % 3 == 0) and x != 8:
         print("---|---|---")
         
def rowNeigh(row): #Finding a cell's neighbors in their row
      checkR = ""
      #numR = int(num / 9)
      tempR = matrix[int(row)]
      for r in range(len(matrix)):
         checkR = checkR + tempR[r]
      return checkR
         
def colNeigh(col): #Finding a cell's neighbors in their column
      checkC = ""
      #numC = int(num % 9)
      for c in range(len(matrix)):
         tempC = matrix[c]
         checkC = checkC + tempC[col]
      return checkC
         
def boxNeigh(row, col): #Finding a cell's neighbors in their 3x3 box
      checkB = ""
      if(row >= 0 and row <= 2 and col >= 0 and col <= 2): 
         for temp in range(3):
            box = matrix[temp]
            for b in range(3): 
               checkB = checkB + box[b]
      if(row >= 0 and row <= 2 and col >= 3 and col <= 5):
         for temp in range(3):
            box = matrix[temp]
            for b in range(3,6,1): 
               checkB = checkB + box[b]
      if(row >= 0 and row <= 2 and col >= 6 and col <= 8):
         for temp in range(3):
            box = matrix[temp]
            for b in range(6,9,1): 
               checkB = checkB + box[b]
      if(row >= 3 and row <= 5 and col >= 0 and col <= 2):
         for temp in range(3,6,1):
            box = matrix[temp]
            for b in range(3): 
               checkB = checkB + box[b]
      if(row >= 3 and row <= 5 and col >= 3 and col <= 5):
         for temp in range(3,6,1):
            box = matrix[temp]
            for b in range(3,6,1): 
               checkB = checkB + box[b]
      if(row >= 3 and row <= 5 and col >= 6 and col <= 8):
         for temp in range(3,6,1):
            box = matrix[temp]
            for b in range(6,9,1): 
               checkB = checkB + box[b]
      if(row >= 6 and row <= 8 and col >= 0 and col <= 2):
         for temp in range(6,9,1):
            box = matrix[temp]
            for b in range(3): 
               checkB = checkB + box[b]
      if(row >= 6 and row <= 8 and col >= 3 and col <= 5):
         for temp in range(6,9,1):
            box = matrix[temp]
            for b in range(3,6,1): 
               checkB = checkB + box[b]
      if(row >= 6 and row <= 8 and col >= 6 and col <= 8):
         for temp in range(6,9,1):
            box = matrix[temp]
            for b in range(6,9,1): 
               checkB = checkB + box[b]
      return checkB
    
  


def findEmpty(): #THIS WORKS
    meh = []
    for r in range(0, 9, 1):
        temp = matrix[r]
        for c in range(0, 9, 1): 
            if(temp[c] == "."):
               meh.append(r)
               meh.append(c)
               return meh
    return -1,-1 #No more empty cells

def solveSudoku():
   temp = []
   temp = findEmpty()
   erow = temp[0]
   ecol = temp[1]
   
   if erow == -1:
      return True #Sudoku is solved

   r = rowNeigh(erow)
   c = colNeigh(ecol)
   b = boxNeigh(erow, ecol)

   possible = findPossibilities(r,c,b)
   for index in range(len(possible)):
      val = possible[index]
      if checker(val, r, c, b) == True: #If value is valid, then assign the value to the empty cell
         temp = matrix[erow]
         temp[ecol] = val
         matrix[erow] = temp
         if solveSudoku(): #If this function had returned True earlier ("i == -1"), program is finished
            return True
         temp = matrix[erow]  # Undo the current cell for backtracking
         temp[ecol] = "."
         matrix[erow] = temp
   return False

def oneChoiceR(r):      #Checks if there is one possibility in row
   num = 0
   for x in range(len(r)):
      if r[x:(x+1)] == ".":
         num = num + 1
   return num

def oneChoiceC(c):      #Checks if there is one possibility in col
   num = 0
   for x in range(len(c)):
      if c[x:(x+1)] == ".":
         num = num + 1
   return num

def oneChoiceB(b):      #Checks if there is one possibility in box
   num = 0
   for x in range(len(b)):
      if b[x:(x+1)] == ".":
         num = num + 1
   return num
            
def findPossibilities(r,c,b): #Finding all the possible values for a cell 
   possible = []

   if oneChoiceR(r) == 1:     #One choice for the val's row
      for x in range(1,10,1):
         num1 = str(x)
         if num1 not in r:
            possible.append(num1)
            return possible

   if oneChoiceC(c) == 1:     #One choice for the val's col
      for x in range(1,10,1):
         num1 = str(x)
         if num1 not in c:
            possible.append(num1)
            return possible

   if oneChoiceB(b) == 1:     #One choice for the val's box
      for x in range(1,10,1):
         num1 = str(x)
         if num1 not in b:
            possible.append(num1)
            return possible

   for x in range(1,10,1):    #Intersection between val's row, col, and box
      tempo = str(x) 
      if((tempo not in b) and (tempo not in c) and (tempo not in r)): #Single Possibility Rule
         possible.append(tempo)
   return possible

def checker(val, r, c, b): #Checking the value of the empty cell
   possible = []
   if((val not in r) and (val not in c) and (val not in b)): #Checking that if a specific value is not in a row, column, and 3x3 box
      return True
   return False
   
for x in range(128):
  tic = time()
  print("Problem #: " + str(x+1))
  createMatrix(x)
  solveSudoku()
  display(matrix)
  matrix = []
  print()
  toc = time()
  print() 
  print( 'Time = %f seconds' % ( toc - tic ) )
  



