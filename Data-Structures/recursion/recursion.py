# ======================= #
# ------ Recursion ------ #
# ======================= #


# Sum numbers up to n

def add(n):
    if n == 0:
        return n
    else:
        return n + add(n-1)


# print(add(6))
# >>> 21


# All posible routes of an n*m grid, moving left and down only


def path(n, m):
    if m == 1 or n == 1:
        return 1
    else:
        return path(n-1, m) + path(n, m-1)


# print(path(2, 3))
# >>> 3



# Count partitions
# ---

# Write a function that counts the number of ways you can partition n objects using parts up to m
# Constraints: m, n >= 0


def partitions(m, n):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return partitions(n-m, m) + partitions(n, m-1)


print(partitions(7, 3))
# >>> 5

# ============================================= #
# ---------- More recursive problems ---------- # 
# ============================================= #



# Recursion: Array Sum
# ---

# Write a function that finds the sum of a list. Make your function recursive.

def sum_recursively(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[-1] + sum_recursively(lst[:-1])



# The Fibonacci Number
# ---

# Create a function that, given a number, returns the corresponding value of that index in the Fibonacci series.


def fibonacci(num):
	if num <= 1:
		return 1
	return fibonacci(num-1) + fibonacci(num-2)



# Combinatorial Exploration
# ---

# Given a known number of unique items, how many ways could we arrange them in a row?



def no_perms_digits(n):
  if n == 0: return 1
  def perms(n):
    if n == 1:
      return n
    return n * perms(n-1)
  return len(str(perms(n)))


# Minnimum swaps from one binary to another
# ---

def min_swaps(s1, s2, count=0):
    if len(s1) == 0:
        return count/2
    if s1[-1] != s2[-1]:
        count += 1
    return min_swaps(s1[:-1], s2[:-1], count)


print(min_swaps("1100", "1001"))



















