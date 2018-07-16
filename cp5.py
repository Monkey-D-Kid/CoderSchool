def checkpoint5_problem2(i_List):
  s_set = set()
  longest = 0
  for i in i_List:
    s_set.add(i)

  for num in i_List:
    length = 1
    next_number = num + 1
    while next_number in s_set:
      length += 1
      next_number += 1

    if length > longest:
      longest = length

  return longest

