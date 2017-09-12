from math import cos
from math import sin
from math import atan2
temp = open('circleO.ppm').read().split()
array = temp[4:]

comp = []
gval = []
counter = 0
index = 0
num = 0
temp1 = 0
gX = 0
gY = 0 
g = 0
threshold = 60
angle = 0
g1 = 0 
g2 = 0
angle = 0
angles = []   
   
radius = 0
xcenter = 0
ycenter = 0
x = 0
y = 0 
center = 0
   
output = open("findCircle.ppm", 'w')
output.write('P3\n')
output.write('640 480\n')
output.write('255\n')
   
for x in range(0,len(array),3): #COMPRESS
  num = int((0.3 * float(array[x])) + (0.59 * float(array[x+1])) + (0.11 * float(array[x+2])))
  comp.append(num)
  
#for x in range(len(comp)):
   #if comp[x] != 255:
     #counter = counter + 1

#There are 304100 pixels out 307200 that are part of the circle


for r in range(480):  #GVALUES 
  for c in range(640):
    num = (r*640) + c
    if((r == 0) or (r == 479) or (c == 0) or (c == 639) or comp[num] != 255):    #Bounds
       angles.append(0)
       #counter = counter + 1
    else:
       topl = (comp[num - 640 - 1])
       topm = (comp[num - 640])
       topr = (comp[num - 640 + 1])
       midl = (comp[num - 1])
       midm = (comp[num]) 
       midr = (comp[num + 1])
       botl = (comp[num + 640 - 1])
       botm = (comp[num + 640])
       botr = (comp[num + 640 + 1])
          
       gX = (-1*topl) + (0*topm) + (1*topr) + (-2*midl) + (0*midm) + (2*midr) + (-1*botl) + (0*botm) + (1*botr)
       gY = (-1*topl) + (-2*topm) + (-1*topr) + (0*midl) + (0*midm) + (0*midr) + (1*botl) + (2*botm) + (1*botr)
 

 #print(counter)


       
for x in range(480):  
  for y in range(640):
    num = (x*640) + y
    if((x != 0) and (x != 479) and (y != 0) and (y != 639) and comp[num] == 255):    #Bounds
       for r in range(0,2,(x**2 + y**2)**0.5):
          xi = x + r*cos(angles[num])
          yi = y + r*sin(angles[num])
       
    
          
