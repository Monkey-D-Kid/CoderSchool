def add_border_nth_to_matrix(matrix, n):
  size = n*2-1
  target = []
  for r in range(size):
    row = []
    for c in range(size):
      if r == 0 or r == (size-1):
        row.append(n)
      elif c == 0 or c == (size-1):
        if not row:
            row = matrix[r-1]
        row.insert(c,n)
    target.append(row)
  return target

def checkpoint2(n):
  if n == 0:
    return []
  elif n == 1:
    return [1]
  else:
    matrix = [[1]]
    for i in range(2,n+1):
      matrix = add_border_nth_to_matrix(matrix, i)
  return matrix
