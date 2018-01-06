#
# Numan Khan 
#
import pickle

pkl_file = open('myfile.pkl', 'rb')
runtime = pickle.load(pkl_file)
pkl_file.close()

def checkLongest(longest, loc):
   for x in range(128):
      if (runtime[x] > 2000): 
      	print("Problem " + str(x+1) + "'s runtime: " + str(runtime[x]))
   
   
longest = 0
loc = for
#0 x in range(128):
#	print("Problem " + str(x+1) + "'s runtime: " + str(runtime[x]))
checkLongest(longest, loc)
