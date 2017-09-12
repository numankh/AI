#
#   Numan Khan 10/8/15
import pickle
#from collections import defaultdict
loc = open('romEdges.txt').read().split()
#word = input("Enter a key: ")

dict = {}
list = []   
list2 = []


      
      
for x in range(0,len(loc),2):
   list = []
   list2 = []
   if loc[x] in dict.keys():
      list = dict[loc[x]]
      list.append(loc[x+1])
      dict[loc[x]] = list
   else:
      #list = dict[loc[x]]
      list.append(loc[x+1])
      dict[loc[x]] = list
      list = []
      
   if loc[x+1] in dict.keys():
      list2 = dict[loc[x+1]]
      list2.append(loc[x])
      dict[loc[x+1]] = list2
   else:
      #list = dict[loc[x+1]]
      list2.append(loc[x])
      dict[loc[x+1]] = list2
      list2 = []

print(dict)

output = open('romNeigh.pkl', 'wb')
pickle.dump(dict, output)
output.close()

