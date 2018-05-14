#Practicing functions in Python

# Write your square_root function here:
def square_root(num):
  return num**.5


# Uncomment these function calls to test your square_root function:
#print(square_root(16))
# should print 4
#print(square_root(100))
# should print 10

# Write your introduction function here:
def introduction(first_name, last_name):
  intro_string = last_name + ", " + first_name + " " + last_name
  return intro_string



# Uncomment these function calls to test your introduction function:
#print(introduction("James", "Bond"))
# should print Bond, James Bond
#print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# Write your tip function here (essentially how much should you tip given a
# total and percentage to tip)
def tip(total, percentage):
  return (total * (1 + percentage*.01)) - total


# Uncomment these function calls to test your tip function:
#print(tip(10, 25))
# should print 2.5
#print(tip(0, 100))
# should print 0.0

# Write your win_percentage function here:
def win_percentage(wins, losses):
  total_games = wins + losses
  return (wins / total_games) * 100


# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100

# Write your first_three_multiples function here (it should print 3 lines, and return the 3rd multiple:

def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

# Uncomment these function calls to test your first_three_multiples function:
#first_three_multiples(10)
# should print 10, 20, 30, and return 30
#first_three_multiples(0)
# should print 0, 0, 0, and return 0


# Write your dog_years function here:

def dog_years(name, age):
  dog_age = age * 7
  return name + ", you are " + str(dog_age) + " years old in dog years"


# Uncomment these function calls to test your dog_years function:
#print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
#print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"


# Write your remainder function
#(The function should return the remainder of twice num1 divided by half of num2.) here:

def remainder(num1, num2):
  return (2 * num1) % (.5 * num2)


# Uncomment these function calls to test your remainder function:
#print(remainder(15, 14))
# should print 2
#print(remainder(9, 6))
# should print 0


# Write your lots_of_math function here:
# The function should print 4 lines.
# First, the sum of a and b.
# Second, d subtracted from c.
# Third, the first number printed, multiplied by the second number printed.
# Finally, it should return the third number printed mod a.

def lots_of_math(a,b,c,d):
  nl = "\n"
  first = a + b
  second = c - d
  third = first * second

  print(str(first) + nl + str(second) + nl + str(third))

  return third % a


# Uncomment these function calls to test your lots_of_math function:
#print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
