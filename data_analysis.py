# Data Analysis and Visualization of file data.csv used for this project

import matplotlib.pyplot as plt
import csv
import math

x1 = []
y1 = []

with open("data.csv") as csvDataFile: # for storing data from rows
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    x1.append(math.floor(float(row[0])))
    y1.append(math.floor(float(row[1])))

# Statistics
print("1st rows values range from "+str(min(x1))+" to "+str(max(x1))+" with average of "+str((float(sum(x1)))/len(x1)) )
print("2nd rows values range from "+str(min(y1))+" to "+str(max(y1))+" with average of "+str((float(sum(y1)))/len(y1)) )

# Visualize
plt.scatter(x1,y1, label= "stars", color = "green", marker = "*", s=30)

plt.xlabel('x-axis: Row 1')
plt.ylabel('y-axis: Row 2')
plt.title('Dataset scatter plot!')
plt.legend()
plt.show()
