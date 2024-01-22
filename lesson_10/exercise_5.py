# Exercise 5:
# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.


n = int(input())

f = 0
fi = 1
fib = 1
while fib <= n:
    print(fib)
    fib = fi + f
    f = fi
    fi = fib

