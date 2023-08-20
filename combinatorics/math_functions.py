import math

def get_factorial(x):
	return math.factorial(x)

def get_power(x, n): # base value, power value 
	return math.pow(x, n) 

def a_or_b(x, y):
	return x + y

def a_and_b(x, y):
	return x * y

def multiply_list(some_List):
    res = 1
    for x in some_List:
        res *= x
    return res

# ================================================

def get_simple_probability(m, n): # m - outcomes of interest, n - total number of outcomes
    return m / n

def get_permutation_with_rep(n, k): # n - population, k - sample
	return get_power(n, k)

def get_permutation_without_rep(n, k): 
	return get_factorial(n) / get_factorial(n - k)


def get_combination_with_rep(n, k):
	return (n + k - 1) / (get_factorial(k) * get_factorial(n - 1))

def get_combination_without_rep(n, k):
	return get_factorial(n) / (get_factorial(n - k) * get_factorial(k))