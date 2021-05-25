#Author: Jesús Rodríguez Corrochano

#Import the needed libraries
import json
import matplotlib.pyplot as plt

#Load the data
List = json.load(open("Random_List.json"))

#Calculate the times each number appears (frequency)
Number = []
Frequency = []
for i in range(0,101):
    freq = 0
    for j in List:
        if  i == j:
            freq = freq + 1
    Number.append(i)
    Frequency.append(freq)
    
#Bar plot visualization with the frequency of each number
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(Number, Frequency)
plt.title("Frequency")
plt.savefig('Bar_Plot_Visualization.png')