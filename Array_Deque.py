from Deque import Deque

class Array_Deque(Deque):
  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity

  def __str__(self):
    return str(self.__contents)

  def __len__(self):
    return self.__capacity

  def __grow(self):
    oldsize = self.__capacity
    self.__capacity *= 2
    self.__contents = self.__contents + [None] * oldsize

  def push_front(self, val):
    if self.__contents[self.__capacity-1] != None:
      self.__grow()

    cursize = self.__capacity

    for i in range(cursize,0,-1):

      if self.__contents[i-1] == None:
        pass
      else:
        self.__contents[i] = self.__contents[i-1]

    self.__contents[0] = val

  def pop_front(self):
    val = self.__contents[0]

    for i in range(self.__capacity):
      
      if (self.__contents[i] == None or i == self.__capacity-1):
        self.__contents[i] = None
        pass
      else:
        self.__contents[i] = self.__contents[i+1]
    return val

  def peek_front(self):
    return self.__contents[0]

  def push_back(self, val):
    if self.__contents[self.__capacity-1] != None:
      self.__grow()

    for i in range(self.__capacity):
      if (self.__contents[i] != None):
        pass
      else:
        self.__contents[i] = val
        break      

  def pop_back(self):
    counter = self.__capacity-1
    while self.__contents[counter] == None:
      counter -= 1
    val = self.__contents[counter]
    self.__contents[counter] = None
    return val

  def peek_back(self):
    counter = self.__capacity-1
    while self.__contents[counter] == None:
      counter -= 1
    return self.__contents[counter]
    


# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
 



