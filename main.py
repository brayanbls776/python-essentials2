from sys import path

from module import suml, prodl


for p in path:
  print(p)
 
zeroes = [i for i in range(5)]
ones = [i + 1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))
print(zeroes)

