class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      self._val = val
      self._next = None
      self._previous = None
     

  def __init__(self):
    self._Header = self._Node(None)
    self._Trailer = self._Node(None)
    self._Header._next = self._Trailer
    self._Trailer._previous = self._Header
    self._size = 0
   

  def __len__(self):
    return self._size
   

  def append_element(self, val):
    newest = self._Node(val)
    newest._next = self._Trailer
    newest._previous = self._Trailer._previous
    self._Trailer._previous._next = newest
    self._Trailer._previous = newest
    self._size += 1
   

  def insert_element_at(self, val, index):
    if (index < 0 or index >= self._size):
      raise IndexError
    newest = self._Node(val)
    if (index <= self._size//2):
      cur = self._Header._next
      for i in range (index):
        cur = cur._next
    else:
      cur = self._Trailer
      for i in range (self._size - index):
        cur = cur._previous
    newest._next = cur
    newest._previous = cur._previous
    cur._previous._next = newest
    cur._previous = newest
    self._size += 1
   

  def remove_element_at(self, index):
    if (index < 0 or index >= self._size):
      raise IndexError
    if (index <= self._size//2):
      cur = self._Header._next
      for i in range (index):
       cur = cur._next
    else:
      cur = self._Trailer
      for i in range (self._size - index):
        cur = cur._previous
    val = cur._val
    cur._previous._next = cur._next
    cur._next._previous = cur._previous
    self._size -= 1
    return val
    

  def get_element_at(self, index):
    if (index < 0 or index >= self._size):
      raise IndexError
    if (index <= self._size//2):
      cur = self._Header._next
      for i in range (index):
       cur = cur._next
    else:
      cur = self._Trailer
      for i in range (self._size - index):
        cur = cur._previous
    return cur._val
   

  def rotate_left(self):
    if (self._size <= 1):
      return
    val = self.remove_element_at(0)
    self.append_element(val)
    
    
  def __str__(self):
    if (self._size == 0):
     return '[ ]'
    else:
      string = '[ ' + str(self._Header._next._val)
      cur = self._Header._next._next
      while (cur is not self._Trailer):
        string += ', ' + str(cur._val)
        cur = cur._next
      return string + ' ]'
          

  def __iter__(self):
    self.__iter_index = 0 
    return self

  def __next__(self):
    if (self.__iter_index == self._size):
     raise StopIteration
    val = self.get_element_at(self.__iter_index)
    self.__iter_index += 1
    return val
    

if __name__ == '__main__':

  test = Linked_List()
  print (test)            #testing __str__() works with empty ll
  
  try:
    test.remove_element_at(0)  #testing empty ll removal and error
  except IndexError:
    print ('Error: Invalid index')
  print (test)
  
  test.append_element(5)  #testing append
  test.append_element(4)
  test.append_element(8)
  test.append_element(1)
  print (test) 
  print ("Expected size: 4 ")
  print ("Actual size: " + str(test._size))           #testing __str__()
  
  test.rotate_left()      #testing rotate_left()
  print (test)
  
  try:
   test.insert_element_at(10,1)  #testing insert at correct index before len/2
   test.insert_element_at(33,4)   #testing insert at correct index past len/2
   test.insert_element_at(20,6)   #testing won't insert
  except IndexError:              #testing error for insert at index 6
    print('Error: Invalid index')
  print (test)
  
  try: 
    test.remove_element_at(1)    #testing remove correct index before len/2
    test.remove_element_at(3)    #testing remove correct index past len/2
    test.remove_element_at(4)     # testing won't remove 
  except IndexError:              #testing error for remove at index 4
    print('Error: Invalid index')
  print (test)
  
  try:
    print (test.get_element_at(0))  #testing get_element_at before len/2
    print (test.get_element_at(3))   #testing get_element_at past len/2
    test.get_element_at(20)    #testing error for get_element_at(index=20)
  except IndexError:
    print ('Error: Invalid index')
    
  for val in test:            #testing iterator
    print (val) 
  
  