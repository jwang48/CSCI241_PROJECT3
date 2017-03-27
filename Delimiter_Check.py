import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  parendq = Stack()
  brackdq = Stack()
  curlydq = Stack()

  f = open (filename, 'r')

  bigstring = f.read()

  for letter in range(len(bigstring)):

    if bigstring[letter] == "(":
      parendq.push(bigstring[letter])
    elif bigstring[letter] == "[":
      brackdq.push(bigstring[letter])
    elif bigstring[letter] == "{":
      curlydq.push(bigstring[letter])

    if bigstring[letter] == ")":
      if parendq.peek() != "(":
        return False 
      else:
        parendq.pop()
    elif bigstring[letter] == "]":
      if brackdq.peek() != "[":
        return False 
      else:
        brackdq.pop()

    elif bigstring[letter] == "}":
      if curlydq.peek() != "{":
        return False 
      else:
        curlydq.pop()

  if parendq.__len__() > 0:
    return False
  elif brackdq.__len__() > 0:
    return False
  elif curlydq.__len__() > 0:
    return False
  else:
    return True


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']

  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


