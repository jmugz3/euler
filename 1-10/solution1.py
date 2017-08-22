#!/usr/bin/env python3

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1

"""

input = [x for x in range(0, 10)]
test = [x for x in range(0, 1000)]


def multiple3or5(input):
    if not input:
        return 0
    else:
        agg = 0
        for digit in input:
            print("digit {0}".format(digit))
            if digit % 3 == 0 or digit % 5 == 0:
                agg += digit
                print("agg: {0}".format(agg))
            else:
                continue
    return agg


def sum_of_sequence(n):
    """
        Using N(N+1)/ 2
    """
    if not input:
        return 0
    else:
        return (n*(n+1))/2


print(multiple3or5(input))
print(multiple3or5(test))

print("Using Arithmetic")
print(int(3*sum_of_sequence(999//3) + 5*sum_of_sequence(999//5) -
      15*sum_of_sequence(999//15)))
