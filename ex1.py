# Exercise 1

"""
Q1) This code defines a recursive function named func that calculates the nth Fibonacci number.
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

    Here's a breakdown of how the code works:

    - If n is 0 or 1, the function returns n (base cases).
    - If n is greater than 1, the function recursively calls itself twice with n-1 and n-2,
      and then returns the sum of these two recursive calls.

    The recursive nature of the function means that it will continue breaking down the problem into smaller subproblems
    until it reaches the base cases (n equals 0 or 1), at which point it starts returning values back up the recursion stack
    to compute the final result.

    For example, if you call func(5), it would compute the 5th Fibonacci number by summing the 4th and 3rd Fibonacci numbers,
    which in turn are computed by summing the 3rd and 2nd Fibonacci numbers, and so on, until it reaches the base cases.

Q2) No, the Fibonacci algortm being analysed is an example of a recursive algorithm, but it doesn't fit the typical definition of a "divide and conqueror" algorithm.
    In a divide and conqueror algorithm, a problem is broken down into smaller subprblems of the same type, and these subprblems are soved independently. The solutions to the subproblems are then combined to solve the oriinal problem. 

Q3) The time complexity of the provided Fibonacci algorithm is exponential, specifically O(2^n), where n is the input parameter.

    Here's a brief explanation:

    - Each recursive call leads to two more recursive calls (func(n-1) and func(n-2)).
    - The branching factor is 2, and the recursion depth is n.

    Therefore, the number of function calls grows exponentially with the input size, resulting in an exponential time complexity. This is not an efficient algorithm for large values of n due to the repeated and redundant calculations, and there are more efficient ways to compute Fibonacci numbers, such as using dynamic programming techniques like memoization or bottom-up approaches, which can reduce the time complexity to O(n).

    In terms of an equation, the time complexity can be given as follows:
    T(n) = T(n-1) + T(n-2) + O(1)

Q4) Please Look Below for code 

Q5) T(n) = O(n)

Q6) Please Look Below for code
"""

# Q4)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

# Example usage:
print(fib_memo(10))  # Output: 55


# Q6)
import timeit
import matplotlib.pyplot as plt

def original_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_fibonacci(n-1) + original_fibonacci(n-2)

def improved_fibonacci(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = improved_fibonacci(n-1, memo) + improved_fibonacci(n-2, memo)
    return memo[n]

# Time the original Fibonacci function
original_times = []
for n in range(36):
    time_taken = timeit.timeit(lambda: original_fibonacci(n), number=10)
    original_times.append(time_taken)

# Time the improved Fibonacci function (using memoization)
improved_times = []
for n in range(36):
    time_taken = timeit.timeit(lambda: improved_fibonacci(n), number=10)
    improved_times.append(time_taken)

# Plot the results
plt.plot(range(36), original_times, label='Original Fibonacci')
plt.plot(range(36), improved_times, label='Improved Fibonacci')
plt.xlabel('Input (n)')
plt.ylabel('Time taken (seconds)')
plt.legend()

# Save the plots with specified filenames
plt.savefig('ex1.6.1.jpg')  # Original Fibonacci plot
plt.clf()  # Clear the current figure

plt.plot(range(36), original_times, label='Original Fibonacci')
plt.plot(range(36), improved_times, label='Improved Fibonacci')
plt.xlabel('Input (n)')
plt.ylabel('Time taken (seconds)')
plt.legend()

plt.savefig('ex1.6.2.jpg')  # Improved Fibonacci plot
