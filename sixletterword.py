#
#   Numan Khan 9/10/15
import pickle
words = open('words.txt').read().split()

def isNeigh(word1, word2):
   num1 = 0
   for x in range(0,6):
      if(word1[x] == word2[x]):
         num1 += 1
   if(num1 == 5):
      return True
   else:
      return False
  

dict = {}
list = []     
for x in range(len(words)):
   list = []
   for y in range(len(words)):
      if (isNeigh(words[x], words[y])):
         list.append(words[y])
   dict[words[x]] = list

output = open('myfile.pkl', 'wb')
pickle.dump(dict, output)
output.close()