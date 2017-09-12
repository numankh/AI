#
#   Numan Khan 10/10/15
import pickle
loc = open('romNodes.txt').read().split()
#word = input('Enter a location: ')

 

dict = {}
list = []   
counter = 0

for x in range(0,len(loc) - 3,3):
   if (x < (len(loc) - 3)):
      list.append(loc[x+1])
      list.append(loc[x+2])
      dict[loc[x]] = list
      list = []
   if (x == (len(loc) - 3)):
      list.append(loc[x+1])
      list.append(loc[x+2])
      dict[loc[x]] = list

print(dict)  

output = open('romCoord.pkl', 'wb')
pickle.dump(dict, output)
output.close()
