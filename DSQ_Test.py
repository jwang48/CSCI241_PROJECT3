import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    # Run your tests with each deque type to ensure that
    # they behave identically.
      self.__deque = get_deque(LL_DEQUE_TYPE)
      self.__stack = Stack()
      self.__queue = Queue()

        
  def test_empty_list_deque(self):
      self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')
    
  def test_empty_list_Queue(self):
      self.assertEqual('[ ]', str(self.__queue), 'Empty list should print as "[ ]"')
    
  def test_empty_list_Stack(self):
      self.assertEqual('[ ]', str(self.__stack), 'Empty list should print as "[ ]"')    
        
  def test_get_empty_length_deque(self):
      self.assertEqual(0, len(self.__deque))

  def test_get_empty_length_stack(self):
      self.assertEqual(0, len(self.__stack))
      
        
  def test_push_front_deque_empty(self):
      self.__deque.push_front(0)
      self.assertEqual('[ 0 ]', str(self.__deque))
            
  def test_push_front_deque_one(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1)
      self.assertEqual('[ 1, 0 ]', str(self.__deque))
    
  def test_push_front_length_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1)
      self.assertEqual(2, len(self.__deque))    
        
  def test_push_back_deque_empty(self):
      self.__deque.push_back(0)
      self.assertEqual('[ 0 ]', str(self.__deque))
              
  def test_push_back_deque_one(self):
      self.__deque.push_back(0)
      self.__deque.push_back(1)
      self.assertEqual('[ 0, 1 ]', str(self.__deque))
      
  def test_push_back_length_deque(self):
      self.__deque.push_back(0)
      self.__deque.push_back(1)
      self.assertEqual(2, len(self.__deque))

  def test_peek_front_one_deque(self):
      self.__deque.push_front(0) 
      returned = self.__deque.peek_front()
      self.assertEqual('[ 0 ]', str(self.__deque))

  def test_peek_front_two_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1) 
      returned = self.__deque.peek_front()
      self.assertEqual('[ 1, 0 ]', str(self.__deque))

  def test_peek_back_value_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1) 
      self.assertEqual( 0, self.__deque.peek_back())    
      
  def test_peek_back_empty_deque(self):
      self.assertEqual(None,self.__deque.peek_back())    

  def test_peek_back_one_deque(self):
      self.__deque.push_front(0) 
      returned = self.__deque.peek_back()
      self.assertEqual('[ 0 ]', str(self.__deque))
      
  def test_peek_back_two_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1) 
      returned = self.__deque.peek_back()
      self.assertEqual('[ 1, 0 ]', str(self.__deque))

      
  def test_pop_front_empty_deque(self):
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_one_deque(self):
      self.__deque.push_front(0)
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
      
  def test_pop_front_two_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.assertEqual('[ 0 ]', str(self.__deque))

      
  def test_pop_front_length_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.assertEqual(1, len(self.__deque))
      
  def test_pop_front_value_deque(self):
      self.__deque.push_back(0)
      self.__deque.push_back(1)
      self.assertEqual(0, self.__deque.pop_front())        

  def test_pop_back_empty_deque(self):
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_one_deque(self):
      self.__deque.push_front(0)
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
          
  def test_pop_back_two_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.assertEqual('[ 1 ]', str(self.__deque))
      
  def test_pop_back_value_deque(self):
      self.__deque.push_back(0)
      self.__deque.push_back(1)
      self.assertEqual(1, self.__deque.pop_back())

  def test_pop_back_length_deque(self):
      self.__deque.push_front(0)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.assertEqual(1, len(self.__deque))
      
  def test_push_stack_empty(self):
      self.__stack.push(0)
      self.assertEqual('[ 0 ]', str(self.__stack))

  def test_push_stack_one(self):
      self.__stack.push(0)
      self.__stack.push(1)
      self.assertEqual('[ 1, 0 ]', str(self.__stack))
      
  def test_push_stack_two(self):
      self.__stack.push(0)
      self.__stack.push(1)
      self.__stack.push(2)
      self.assertEqual('[ 2, 1, 0 ]', str(self.__stack))    
      
  def test_push_length_stack(self):
      self.__stack.push(0)
      self.__stack.push(1)
      self.assertEqual(2, len(self.__stack))
      
  def test_pop_stack_two(self):
      self.__stack.push(0)
      self.__stack.push(1)
      self.__stack.pop()
      self.assertEqual('[ 0 ]', str(self.__stack))

  def test_pop_stack_one(self):
      self.__stack.push(0)
      self.__stack.pop()
      self.assertEqual('[ ]', str(self.__stack))

  def test_pop_empty_stack(self):
      self.assertEqual('[ ]', str(self.__stack))

  def test_pop_stack_value(self):
      self.__stack.push(0)
      self.__stack.push(1)
      self.assertEqual(1, self.__stack.pop())
      
  def test_peek_value_stack(self):
      self.__stack.push(0)
      self.__stack.push(1)
      self.assertEqual(1, self.__stack.peek())                 

  def test_peek_empty_stack(self):
      self.assertEqual(None, self.__stack.peek())
      
  def test_peek_one_stack(self):
      self.__stack.push(0)
      returned = self.__stack.peek()
      self.assertEqual('[ 0 ]', str(self.__stack))   

  def test_peek_two_stack(self):
      self.__stack.push(0)
      self.__stack.push(1)
      returned = self.__stack.peek()
      self.assertEqual('[ 1, 0 ]', str(self.__stack))       

  def test_get_empty_length_queue(self):
      self.assertEqual(0, len(self.__queue))

  def test_enqueue_empty(self):
      self.__queue.enqueue(0)
      self.assertEqual('[ 0 ]', str(self.__queue))
      
  def test_enqueue_one_element(self):
      self.__queue.enqueue(0)
      self.__queue.enqueue(1)
      self.assertEqual('[ 0, 1 ]', str(self.__queue))    

  def test_enqueue_two_elements(self):
      self.__queue.enqueue(0)
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.assertEqual('[ 0, 1, 2 ]', str(self.__queue))  

  def test_enqueue_length(self):
      self.__queue.enqueue(0)
      self.__queue.enqueue(1)
      self.assertEqual(2, len(self.__queue))

  def test__dequeue_length(self):
      self.__queue.enqueue(0)
      self.__queue.enqueue(1)  
      self.__queue.dequeue()
      self.assertEqual(1 ,len(self.__queue))

  def test__dequeue_value(self):
      self.__queue.enqueue(0)
      self.__queue.enqueue(1)
      self.assertEqual(0, self.__queue.dequeue())    

  def test__dequeue_empty(self):
      self.assertEqual(None, self.__queue.dequeue())
     
  def test__dequeue_one_element(self):
      self.__queue.enqueue(0)
      self.__queue.dequeue()  
      self.assertEqual('[ ]',str(self.__queue))

  def test__dequeue_two_elements(self):
      self.__queue.enqueue(0)
      self.__queue.enqueue(1)  
      self.__queue.dequeue()
      self.assertEqual('[ 1 ]' ,str(self.__queue))
      
  

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
  unittest.main()

