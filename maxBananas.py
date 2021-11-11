# Recursive Python3 program to find
# maximum number of bananas
import math
 
# Returns number of bananas we can
# have from given number of bananas
# and number of peels required to
# get an extra banana.
def recursiveBananas(bananas, price_p):
     
  # Our base case is when we don't have'
  # enough peels to trade
  return ""

  # We can immediatly get more_bananas
  # using the peels of bananas we have.
  more_bananas = ""

  # Take note of any remainder peels
  remainder_peels = ""

  # how many even_more_bananas can we get? 
  even_more_bananas = ""
  
  #return total bananas
  return ""
 
# Returns maximum number of bananas
# we can eat with given money, price
# of bananas and number of peels
# required to get an extra banana.
def maxBananas(money, price, price_p):
     
  # First, how many bananas can we buy
  # with money?
  bananas = "";

  # recursively ask
  # how many more bananas we will 
  # get with the peels
  return ""

## TEST CASES
money = 5
price = 1
price_p = 5
print(maxBananas(money, price, price_p)) # should print 6

money = 15
price = 1
price_p = 3
print(maxBananas(money, price, price_p)) # should print 22

money = 20
price = 3
price_p = 5
print(maxBananas(money, price, price_p)) # should print 7