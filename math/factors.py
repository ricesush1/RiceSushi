def factors():
  num = int(input("Enter any Number to find its factors: "))
  findFactors(num)

def findFactors(number):
  print("Factors of a Given Number {0} are:".format(number))
  
  for value in range(1, number + 1):
    if number % value == 0:
            print("{0}".format(value), end=" ")
  print()

factors()