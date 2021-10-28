import numpy as np
from array import array

def seatsfilled(seatcount):
  seats = array('b', [0 for i in range(seatcount)])
  insertorder = array('l', np.random.permutation(seatcount-1))
  for idx in insertorder:
    if seats[idx] == 0 and seats[idx+1] == 0:
      seats[idx] = 1
      seats[idx + 1] = 1
  return sum(seats) / seatcount

rsqe = 1 / (2.71828182845904523536 ** 2)
iterations = 8192

for i in range(20):
  print(f"log₂ difference between avg seats unfilled and ℯ⁻² for 2**{i} seats:")
  print(np.log2(np.abs(rsqe - np.average([1 - seatsfilled(2 ** i) for j in range(iterations)]))))
