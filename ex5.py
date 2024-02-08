import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time_search(search_func, arr, target, number=100):
    time = timeit.timeit(lambda: search_func(arr, target), number=number)
    return time / number

def linear_fit(x, a, b):
    return a * x + b

def logarithmic_fit(x, a, b):
    return a * np.log(x) + b

# Generate vectors of different sizes
vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

linear_search_times = []
binary_search_times = []

for size in vector_sizes:
    arr = np.arange(size)
    target = np.random.randint(0, size)  # Pick a random element in the vector
    
    # Measure linear search time
    linear_avg_time = measure_time_search(linear_search, arr, target)
    linear_search_times.append(linear_avg_time)
    
    # Measure binary search time
    binary_avg_time = measure_time_search(binary_search, arr, target)
    binary_search_times.append(binary_avg_time)

# Plotting
x = np.array(vector_sizes)
y_linear = np.array(linear_search_times)
y_binary = np.array(binary_search_times)

# Fitting curves
popt_linear, _ = curve_fit(linear_fit, x, y_linear)
popt_logarithmic, _ = curve_fit(logarithmic_fit, x, y_binary)

# Plotting interpolated curves
x_fit = np.linspace(min(x), max(x), 1000)

plt.plot(x_fit, linear_fit(x_fit, *popt_linear), label='Linear Fit (Linear Search)')
plt.plot(x_fit, logarithmic_fit(x_fit, *popt_logarithmic), label='Logarithmic Fit (Binary Search)')
plt.legend()
plt.show()

print("Parameters for Linear Fit (Linear Search):", popt_linear)
print("Parameters for Logarithmic Fit (Binary Search):", popt_logarithmic)
