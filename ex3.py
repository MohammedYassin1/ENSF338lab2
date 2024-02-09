import timeit
import cProfile
def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

# Create a cProfile object
profiler = cProfile.Profile()

# Enable the profiler
profiler.enable()

# Call the functions you want to profile
test_function()
third_function()

# Disable the profiler
profiler.disable()

# Print the profiling results
profiler.print_stats()

#1) A profiler is describes how many calls and how long parts of a program take.
#2)Profiling relates to the runtime of a program and finding bottlenecks while benchmarking is about a measuring preformance
#of a system or measuring preformance of specific parts of code.
#4)Most of the execution time goes to the third function, this is indictated by the relatively high tottime and cumtime.
#while the rest of the functions consume a neglible amount of time in comparison.