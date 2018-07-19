def checkpoint3_problem1(input_array, k):
  sorted_unique_array = [input_array[0]]
  for i in range(1, len(input_array)):
    for j in range(len(sorted_unique_array)-1, -1, -1):
      if sorted_unique_array[j] > input_array[i]:
        sorted_unique_array.insert(j+1, input_array[i])
        break
      elif sorted_unique_array[j] == input_array[i]:
        break
      elif j == 0:
        sorted_unique_array.insert(0, input_array[i])
  return sorted_unique_array[k-1]

def checkpoint3_problem2(input_array, tuple_range):
  counter = 0
  for i in range(len(input_array)):
    sum = input_array[i]
    for j in range(i+1, len(input_array)):
      sum += input_array[j]
      if (tuple_range[0] <= sum) and (sum <= tuple_range[1]):
        counter+=1
      elif sum > tuple_range[1]:
        break
  return counter
