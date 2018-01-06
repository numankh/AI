#
# Numan Khan 10/25/2015
#

words = open('sudoku128.txt').read().split()
matrix = []
#jambo = input('Enter sudoku problem #: ')
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
    
  
def checkMatrix(matrix): #Check if the matrix is solved
   numR = 0
   numC = 0
   numB = 0
   checkerOld = True

   for num in range(81):



      numR = int(num / 9)

      numC = int(num % 9)
      
      checkR = rowNeigh(numR)
      checkC = colNeigh(numC)
      checkB = boxNeigh(numR, numC)

      #print(str(num) + "'s --> " + "Row Number: " + str(numR) + " -- Column Number:" + str(numC))
      
      meh = num + 1
      
      #print()
      #print("Cell Number: " + str(meh))
      #print("Row: " + str(numR + 1) + " Col: " + str(numC + 1))
      #print("Numbers in row: " + rowNeigh(numR))
      #print("Numbers in column: " + colNeigh(numC))
      #print("Numbers in box: " + boxNeigh(numR, numC))
      #print()
      
      possible = []
      
      for x in range(1,9,1):
         tempo = str(x)
         #print(tempo)
         int(tempo)
         if((tempo not in checkB) and (tempo not in checkC) and (tempo not in checkR)): #Checking that a cell's row, column, and 3x3 box have numbers 1 through 8
            possible.append(tempo)
            checkerOld = False
      #print(possible)
   #print("Is this a solution?: " + str(checkerOld))




#emptyR = 0
#emptyC = 0
def findEmpty(row, col): #THIS WORKS
    meh = []
    for r in range(row, 9, 1):
        temp = matrix[r]
        for c in range(col, 9, 1): 
            if(temp[c] == "."):
               meh.append(r)
               meh.append(c)
               print(meh)
               return meh
    return -1,-1 #No more empty cells
  

#erow = 0
#ecol = 0

def solveSudoku(row, col):
   temp = []
   temp = findEmpty(0, 0)
   erow = temp[0]
   ecol = temp[1]
   #erow,ecol = findEmpty(row, col)
   if erow == -1:
      return True #Sudoku is solved
   possible = findPossibilities(erow,ecol)
   for index in range(len(possible)):
      val = possible[index]
      if checker(val, rowNeigh(erow), colNeigh(ecol), boxNeigh(erow, ecol)) == True: #If value is valid, then assign the value to the empty cell
         temp = matrix[erow]
         temp[ecol] = val
         matrix[erow] = temp
         if solveSudoku(erow, ecol): #If this function had returned True earlier ("i == -1"), program is finished
            return True
                            # Undo the current cell for backtracking
         temp = matrix[erow]
         temp[ecol] = "."
         matrix[erow] = temp
   return False
            
def findPossibilities(row, col):
   #print("Row: " + str(row) + " Col: " + str(col))
   possible = []
   print("Numbers in row: " + rowNeigh(row))
   print("Numbers in column: " + colNeigh(col))
   print("Numbers in box: " + boxNeigh(row, col))
   for x in range(1,9,1):
      tempo = str(x) 
      if((tempo not in boxNeigh(row, col)) and (tempo not in colNeigh(col)) and (tempo not in rowNeigh(row))): #Checking that a cell's row, column, and 3x3 box have numbers 1 through 8
         possible.append(tempo)
   print(possible)
   return possible

def checker(val, checkRow, checkCol, checkBox):
   possible = []
   if((val not in checkBox) and (val not in checkCol) and (val not in checkRow)): #Checking that if a specific value is not in a row, column, and 3x3 box
      #print("failure at: " + tempo)
      return True
   return False
   



createMatrix(6)
display(matrix)
checkMatrix(matrix)
temp = []
#er = 0
#ec = 0
temp = findEmpty(0, 0) #Finding the first occurence of an empty cell
print(temp)
print("Row: " + str(temp[0]+1) + " Col: " + str(temp[1]+1))
possible = findPossibilities(temp[0], temp[1])

#CHECK CASE 7
