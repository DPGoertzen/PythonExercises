# Just a little shipping calculator using control flow basics

premium_shipping = 125

def ground_shipping(weight):
  flat_fee = 20

  if weight <= 2:
    cost = weight * 1.5 + flat_fee
  elif weight > 2 and weight <=6:
    cost = weight * 3 + flat_fee
  elif weight > 6 and weight <=10:
    cost = weight * 4 + flat_fee
  else:
    cost = weight * 4.75 + flat_fee

  return cost

# print(str(ground_shipping(8.4)))
# should be 53.6

def drone_shipping(weight):
  flat_fee = 0

  if weight <= 2:
    cost = weight * 4.5 + flat_fee
  elif weight > 2 and weight <=6:
    cost = weight * 9 + flat_fee
  elif weight > 6 and weight <=10:
    cost = weight * 12 + flat_fee
  else:
    cost = weight * 14.25 + flat_fee

  return cost

print(str(drone_shipping(1.5)))

# We could refactor that though to use a helper
# function:
def shipping_calc(weight, two_pounds, six_pounds, ten_pounds, over_ten_pounds, flat_fee):

  if weight <= 2:
    cost = weight * two_pounds + flat_fee
  elif weight > 2 and weight <=6:
    cost = weight * six_pounds + flat_fee
  elif weight > 6 and weight <=10:
    cost = weight * ten_pounds + flat_fee
  else:
    cost = weight * over_ten_pounds + flat_fee

  return cost

def ground_shipping(weight):
  return shipping_calc(weight, 1.5, 3, 4, 4.75, 20)

def drone_shipping(weight):
  return shipping_calc(weight, 4.5, 9, 12, 14.25, 0)

print(str(ground_shipping(8.4)))
# should be 53.6

print(str(drone_shipping(1.5)))

def cheapest_shipping(weight):
  g = ground_shipping(weight)
  d = drone_shipping(weight)
  p = premium_shipping
  customer_message = "It's cheapest to ship by "
  if g <= d and g <= p:
    cheapest_message = customer_message + "ground"
    print(cheapest_message + "\n$" + str(g))
    return g
  elif d <= g and d <= p:
    cheapest_message = customer_message + "drone"
    print(cheapest_message + "\n$" + str(d))
    return d
  else:
    cheapest_message = customer_message + "premium"
    print(cheapest_message + "\n$" + str(p))
    return p

cheapest_shipping(7)

cheapest_shipping(4.8)
#
cheapest_shipping(41.5)
