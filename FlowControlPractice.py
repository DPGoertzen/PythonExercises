# boolean and flow control exercises

my_baby_bool = "true"

print(type(my_baby_bool))
# <class 'str'>

my_baby_bool_two = True
print(type(my_baby_bool_two))
# <class 'bool'>


def dave_check(user_name):
  if user_name == "Dave" or "angela_catlady_87":
    return "Get off my computer Dave!"


# Enter a user name here, make sure to make it a string
# user_name = "Dave"
# print(dave_check(user_name))
# user_name = "angela_catlady_87"
# print(dave_check(user_name))

def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    return  "I know it is you Dave! Go away!"

# Enter a user name here, make sure to make it a string
user_name = "Dave"

print(dave_check(user_name))

user_name = "angela_catlady_87"

print(dave_check(user_name))

def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"

def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

# both need to evaluate true to be true
def graduation_reqs2(gpa, credits):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

#either need to be True to evaluate True
def graduation_mailer(gpa, credits):
  if gpa >= 2.0 or credits >=120:
    return True

# not (8 * 2) != 20 - 4
# evalutes to true because the interior statement evalues to false

# else statements
def graduation_reqs3(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

# elif practice

def grade_converter(gpa):
  if gpa >= 4.0:
    return "A"
  elif gpa >= 3.0:
    return "B"
  elif gpa >= 2.0:
    return "C"
  elif gpa >= 1.0:
    return "D"
  else:
    return "F"

def raises_value_error():
  raise ValueError

try:
	raises_value_error()
except:
  print("You raised a ValueError!")


def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
