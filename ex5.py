import random
import timeit
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [10, 5]
import numpy as np
from scipy.optimize import curve_fit
import sys
sys.setrecursionlimit(10000)

def findinlist(n, l):
    for i in range(len(l)):
        if l[i] == n:
            return True
    return False

def binary_search(target, arr, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(target, arr, mid + 1, high)  
        else:
            return binary_search(target, arr, low, mid - 1)   
    return -1

def logarithmic_function(x, a, b):
    return a * np.log(x) + b


avgtimes = []
avgtimes_log = []
# For multiple possible input lengths...
listlengths = [1000, 2000, 4000, 8000, 16000, 32000]
for listlength in listlengths:
    # Generate a list of that input length,
    numbers = [x for x in range(listlength)]
    lin = []
    log = []
    # then, consider 1000 different random permutations of that list. For each
    # permutation, time how long it takes to find the number 5 in the list.
    # For increased accuracy, use timeit and ask it to run the test 100 times
    for i in range(1000):
        target = np.random.randint(0, listlength - 1)
        tm = timeit.timeit(lambda: findinlist(target, numbers), number=100)
        lm = timeit.timeit(lambda: binary_search(target, numbers, 0, listlength - 1), number=100) 
        lin.append(tm/100)
        log.append(lm/100)
    # Then, compute the average execution times across all permutations
    # and add it to our list of average times
    avg = sum(lin) / len(lin)
    avg_log = sum(log) / len(log)
    avgtimes.append(avg)
    avgtimes_log.append(avg_log)
    print("Average time for list of length linear %d: %f" % (listlength, avg))
    print("Average time for list of length binary %d: %f" % (listlength, avg_log))

slope, intercept = np.polyfit(listlengths, avgtimes, 1)
plt.scatter(listlengths, avgtimes)

linevalues = [slope * x + intercept for x in listlengths]

popt, _ = curve_fit(logarithmic_function, np.array(listlengths), np.array(avgtimes_log))
a, b = popt

plt.plot(listlengths, linevalues, 'b', label='Linear')
plt.plot(listlengths, logarithmic_function(np.array(listlengths), *popt), 'r', label='Binary')

plt.xlabel('Input Length')
plt.ylabel('Average Time (s)')
plt.title('Fitted Function for Linear and Binary Search Performance')
plt.legend()
plt.show()
# Finally, print out the linear relationship between input length and time.
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
print("Logarithmic function for binary search:")
print("f(x) = {:.2f} * log(x) + {:.2f}".format(a, b))

#4) The linear search had a linear complexity, so the function used was a linear one (ax + b).
#While the binary search had a logarithmic complexity given by the function (a*log(x) + b). The results where unexpected because
#the logarthim fitted function had a slope and y-intercept of 0, this might have been caused a sample size that was too small.