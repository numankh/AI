#
# Numan Khan 10/12/2015
#

import pickle
import queue as Q
from math import pi , acos , sin , cos, sqrt

pkl_file = open('romNeigh.pkl', 'rb')
romNeigh = pickle.load(pkl_file)
pkl_file.close()

pkl1_file = open('romCoord.pkl', 'rb')
romCoord = pickle.load(pkl1_file)
pkl1_file.close()

list = []   
list.append(46.6167)
list.append(21.5167)
romCoord["Z"] = list

#start = input('Enter starting location: ')
#goal = input('Enter location of goal: ')
start = 'A'
goal = 'T'
#
def cost(y1,x1, y2,x2):
   
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   
   R   = 3958.76 # miles
   
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   

              
def heuristic(y1,x1, y2,x2):
    a = (x1, y1)
    b = (x2, y2)
    
    y1  = float(y1)
    x1  = float(x1)
    y2  = float(y2)
    x2  = float(x2)   
    
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
              
def aStar(romNeigh, romCoord, start, goal):
    frontier = Q.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = start
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        list = romNeigh[current]
        for next in range(len(list)):
            list1 = romCoord[current]
            list2 = romCoord[list[next]]
            new_cost = cost_so_far[current] + cost(list1[0],list1[1],list2[0],list2[1])
            if next not in cost_so_far or new_cost < cost_so_far[list[next]]:
                cost_so_far[list[next]] = new_cost
                list3 = romCoord[goal]
                list4 = romCoord[list[next]]
                priority = new_cost + cost(list3[0],list3[1],list4[0],list4[1])
                frontier.put(list[next], priority)
                came_from[list[next]] = current
                
    return came_from, cost_so_far   
                

          
print(aStar(romNeigh, romCoord, start, goal))
