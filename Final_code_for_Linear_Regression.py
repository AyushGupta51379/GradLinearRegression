# comments are used extensively here for simpler understanding

from numpy import *

# 4th step compute errors
def compute_error_for_given_points(b, m, points):
    totalError = 0 # initially error is 0
    # using the average of sum of square of errors
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m*x+b)) **2 # sum of squared errors
    return totalError / float(len(points))

# 3rd step define step gradient function # remember the method here
def step_gradient(b_current, m_current, points, learningRate):
    # define how gradient descent works
    # purpose of gradient descent is to minimize the error by finding minima
    # find where minimum error, giving us y and slope for that minimum error
    # Error = (1/N)(sum i=1 to N of: (( (yi) - m(xi)-b) **2 )) )
    # partial d/dm = (1/N)(2)(sum i=1 to N of: ( (yi) - m(xi) -b)(-xi) )
    # partial d/db = (1/N)(2)(sum i=1 to N of: ( (yi) - m(xi) -b)(-1) )
    # gradient gives us a direction used to get to the minimum error value
    # gradient is a very importtant concept in machine learning
    # gradient descent is a tangent line giving a direction along which we want to move
    # gradient calculation using partial derivatives
    # gradient can be thought of as a bowl problem, we try to go to the minimum point
    # in that bowl
    # if a function is differentiable then we know that we can optimize it
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N)*(y- ((m_current*x)+b_current)) # same formula every time, fundamental law
        m_gradient += -(2/N)*x*(y- ((m_current*x)+b_current)) # same formula every time, fundamental law
    new_b = b_current- (learningRate * b_gradient)
    new_m = m_current- (learningRate * m_gradient)
    return [new_b, new_m]
    

# 2nd step define the model function
def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        # real stuff happens here
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

# 0th step ie. 1st step in data science is to look at data, here we have csv format comfortable for python
# dataset is a set of x and y values, 100 points in 2D
# 1st thing is to parse dataset into memory
def run():
    # points for dataset, use numpy library genfromtext
    points = genfromtxt('data.csv', delimiter = ',') # * for numpy, ',' for splitting sets in data
    learning_rate = 0.0001 # hyperparameter, which can be tuned for our models
    # learning rate defines how fast our model learns # why not a million cause need a bell curve
    # too low lr model too slow to converge, whereas too high model never converge
    # so we want a balance, an optimal learning rate, in actual ml we don't know what is the best value of hyperparameter
    # thus we have to guess and began experimenting
    # line equation y = mx + b, taking initial m and b values as 0s then improving with data set
    initial_b = 0
    initial_m = 0
    num_iterations = 1000 # not taking too much since small dataset
    # ideal b and m values, logic part, using gradient descent runner method
    # feed all defined stuff into the model
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("Line equation form used: y=mx+b")
    print ("Starting gradient descent at b = {0}, m = {1}, Average error = {2}".format(initial_b, initial_m, compute_error_for_given_points(initial_b, initial_m, points)))
    print ("Running...")
    print()
    print("After "+str(num_iterations)+" with "+str(learning_rate)+" learning rate, we get:")
    print("b: "+str(b))
    print("m: "+str(m))
    print("Average error: "+str(compute_error_for_given_points(b, m, points)))
    print("The best fit line equation is y="+str(m)+"x + "+str(b))
    print("Method used: Linear Regression")

if __name__ == '__main__':
    run()
