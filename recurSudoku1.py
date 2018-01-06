#
# Numan Khan 10/25/2015
#

words = open('sudoku128.txt').read().split()
#jambo = input('Enter sudoku problem #: ')

def createMatrix(num):
   matrix = []
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

def findNeigh(matrix): #Find the 20 neighbors of a number
   numR = 0
   numC = 0
   numB = 0

   for num in range(1):

      checkR = ""
      checkC = ""
      checkB = ""

      numR = int(num / 9)
      row = matrix[numR]
      for r in range(len(matrix)):
         checkR = checkR + row[r]

      numC = int(num % 9)
      for c in range(len(matrix)):
         col = matrix[c]
         checkC = checkC + col[numC]

      #print(str(num) + "'s --> " + "Row Number: " + str(numR) + " -- Column Number:" + str(numC))
      
      if(numR >= 0 and numR <= 2 and numC >= 0 and numC <= 2): 
         for temp in range(3):
            box = matrix[temp]
            for b in range(3): 
               checkB = checkB + box[b]
      if(numR >= 0 and numR <= 2 and numC >= 3 and numC <= 5):
         for temp in range(3):
            box = matrix[temp]
            for b in range(3,6,1): 
               checkB = checkB + box[b]
      if(numR >= 0 and numR <= 2 and numC >= 6 and numC <= 8):
         for temp in range(3):
            box = matrix[temp]
            for b in range(6,9,1): 
               checkB = checkB + box[b]
      if(numR >= 3 and numR <= 5 and numC >= 0 and numC <= 2):
         for temp in range(3,6,1):
            box = matrix[temp]
            for b in range(3): 
               checkB = checkB + box[b]
      if(numR >= 3 and numR <= 5 and numC >= 3 and numC <= 5):
         for temp in range(3,6,1):
            box = matrix[temp]
            for b in range(3,6,1): 
               checkB = checkB + box[b]
      if(numR >= 3 and numR <= 5 and numC >= 6 and numC <= 8):
         for temp in range(3,6,1):
            box = matrix[temp]
            for b in range(6,9,1): 
               checkB = checkB + box[b]
      if(numR >= 6 and numR <= 8 and numC >= 0 and numC <= 2):
         for temp in range(6,9,1):
            box = matrix[temp]
            for b in range(3): 
               checkB = checkB + box[b]
      if(numR >= 6 and numR <= 8 and numC >= 3 and numC <= 5):
         for temp in range(6,9,1):
            box = matrix[temp]
            for b in range(3,6,1): 
               checkB = checkB + box[b]
      if(numR >= 6 and numR <= 8 and numC >= 6 and numC <= 8):
         for temp in range(6,9,1):
            box = matrix[temp]
            for b in range(6,9,1): 
               checkB = checkB + box[b]


      print("Numbers in box: " + checkB)
      print("Numbers in column: " + checkC)
      print("Numbers in row: " + checkR)
      print()
      
      for x in range(1,9,1):
         tempo = str(x)
         print(tempo)
         if((tempo not in checkB) and (tempo not in checkC) and (tempo not in checkR)):
            return False # IMPLEMENT STRATS HERE
      return True



display(createMatrix(0))
print(findNeigh(createMatrix(0)))

