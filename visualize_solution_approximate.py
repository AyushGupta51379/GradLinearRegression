import matplotlib.pyplot as plt
import csv
import math
x1=[]
y1=[]

# The line of best fit equation is y=1.4777440851894448x + 0.08893651993741346

with open("data.csv") as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    x1.append(math.floor(float(row[0])))
    y1.append(math.floor(float(row[1])))

xl1 = [25,70] # based on range of 1st row   
yl1 = [37,104] # in line of best fit
yl2 = [68,135] # line above line of best fit, with same slope as of line of best fit
yl3 = [5,72] # line below line of best fit, with same slope as of line of best fit

# Visualize
plt.plot(xl1, yl1, '-r', label = "line of Best fit - line 1")
plt.plot(xl1, yl2, '-r', linestyle='dashed', label = "31pts from line 1 - line 2")
plt.plot(xl1, yl3, '-r', linestyle='dashed', label = "32pts from line 1 - line 3")
plt.scatter(x1,y1, label= "stars", color = "green", marker = "*", s=30)

plt.xlabel('x-axis')
plt.xlabel('y-axis')
plt.title('Linear Regression result scatter plot!')
plt.legend()
plt.show()
