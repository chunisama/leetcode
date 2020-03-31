# This problem is motivated by the need for a company to select a random subset of its 
# customers to roll out a new feature to. For example, a social networking company may 
# want to see the effect of a new UI on page visit duration without taking the chance of 
# alienating all its users if the rollout is unsuccessful.
# Implement an algorithm that takes as input an array of distinct elements and a size, 
# and returns a subset of the given size of the array elements.
# All subsets should be equally likely. Return the result in input array itself.


# iterate thru a index range of 0 to k - 1 => pick a random index from 0 to the length of arr
# after picking random index swap with first index, repeat this step for remaining indices
# this will modify input arr with random subset from 0 to k - 1 
# return a slice of arr between 0 to k - 1

arr = [5, 3, 7, 11] 

import random
def sample_offline_data(arr, k):
  for idx in range(k):
    random_idx = random.randint(idx, len(arr) - 1)
    arr[idx], arr[random_idx] = arr[random_idx], arr[idx]
  return arr[0 : k]

print(sample_offline_data(arr, 3))
  