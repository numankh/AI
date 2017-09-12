#
#   Numan Khan 10/8/15
import pickle
loc = open('romEdges.txt').read().split()

 

dict = {}
list = []   
counter = 0

for x in range(0,len(loc)-1,2):
   if (x < (len(loc) - 2)):
      if (x != 0) and (loc[x] != loc[x+2]):
         list.append(loc[x+1])
         dict[loc[x]] = list      
         list = []
      else:
         list.append(loc[x+1])
   if (x == (len(loc) - 2)):
      list.append(loc[x+1])
      dict[loc[x]] = list

  
print(dict)
output = open('romNeigh.pkl', 'wb')
pickle.dump(dict, output)
output.close()