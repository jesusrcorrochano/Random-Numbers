#Author: Jesús Rodríguez Corrochano

#Import the needed libraries
import random
import json

#Create a list of 1000 random numbers between 0 to 100.
List = []
for i in range(0,1000):
    List.append(random.randrange(101))
    
#Save the output as JSON file
json.dump(List, open("Random_List.json",'w'))