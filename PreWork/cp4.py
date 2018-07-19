class Node:
  def __init__(self, value = None):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def insert_head(self, val):
    node = Node(val)
    node.next = self.head
    self.head = node
    self.size += 1

  def get_size(self):
    return self.size

  def generate_reversed_linkedlist(self, i_LinkedList):
    node = i_LinkedList.head
    while node is not None:
      self.insert_head(node.value)
      node = node.next

def checkpoint4_problem1(i_LinkedList):
  r_LinkedList = LinkedList()
  r_LinkedList.generate_reversed_linkedlist(i_LinkedList)
  r_LinkedList.get_size()
  i_node = i_LinkedList.head
  r_node = r_LinkedList.head
  counter = 1
  while i_node is not None:
    if counter > int(r_LinkedList.get_size()/2):
      break
    else:
      i_node.value = r_node.value - i_node.value
      i_node = i_node.next
      r_node = r_node.next
      counter += 1

def checkpoint4_problem2(i_list):
  o_list = []
  for i in range(len(i_list)):
    if i == (len(i_list)-1):
      o_list.append(-1)
      break

    for j in range(i+1, len(i_list)):
      if i_list[i] < i_list[j]:
        o_list.append(i_list[j])
        break
    else:
      o_list.append(-1)
  return o_list
