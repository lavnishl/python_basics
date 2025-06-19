# https://docs.python.org/3/tutorial/datastructures.html#sets

# my_set={1,2,3,4,5}
# your_set={4,5,6,7,8}
# print(my_set.difference(your_set)) # {1,2,3}
# print(my_set) # {1,2,3,4,5} 

def set_basics_1():
  # unordered collection of elements 
  # without duplicate entries.
  # When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
  # HENCE : used to calculate averages etc 

  # Set is unique elements 
  unique_element_sets = set('abracadabra')
  print(unique_element_sets)

  #  Note: to create an EMPTY set you have to use set(), not {}; the latter creates an empty dictionary,
  empty_set = set()
  empty_dictionary = {} 

  # set uses {...} ... so does MAP ... but map has key:value
  const_set = {1,2,3,4,5}

  myset = set(['a', 'b']) # Creating a set from a list

  # indexed access is not allowed in sets
  # print(my_set[0])

  
def add_vs_update():
  # add(): takes single element , adds a single element, doesn't work with iterable 
  my_set={1,2,3,4,5}
  my_set.add(5) # since it exists nothig added
  print(my_set)
  print(len(my_set))
  # update() : add iterable collection  
  # my_set.add([6,7]]) # TypeError: unhashable type: 'list' 
  # numbers_set.update('x') # TypeError: object is not iterable
  string_alphabet = 'abc'
  numbers_set = {1, 2}
  # add elements of the string to the set
  numbers_set.update(string_alphabet)
  print('numbers_set =', numbers_set)
  
def set_operation_2():
  my_set={1,2,3,4,5}
  my_list = list(my_set)
  print(my_list)

  new_copy = my_set.copy()
  print(new_copy)



def remove_discard_pop(): 
  # https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

  # remove() : (1) If element  does not exist, it RAISES a KeyError. (2) The .remove(x) operation returns None. (3) Original set it modified 
  # ;-) remove is chota , so throw tantrum / error   
  my_set={1,2,3,4,5}
  print(my_set.remove(4)) # None
  print(my_set) # original is modified 
  # print(my_set.remove(6)) # KeyError


  # discard() : (1) If element  does not exist, it DOES NOT give a KeyError. (2) The .remove(x) operation returns None. (3) Original set it modified 
  my_set={1,2,3,4,5}
  print(my_set.discard(4)) # None
  print(my_set) # original is modified 
  print('try to remove element d.n.e')
  print(my_set.discard(6)) # None

  # pop() : removes random element from set & returns the removed element.
  # If there are no elements to remove, it raises a KeyError.
  # pop is sabse chota, hence throw tantrum / error 


def set_join_operations():
  # NONE of these operations modify the original sets 
  # all operations return set

  my_set={1,2,3,4,5}
  your_set={4,5,6,7,8}
  print(my_set.union(your_set))
  print(my_set|your_set) # union = | operator 

  print(my_set.intersection(your_set)) # {4,5} 
  print(my_set&your_set) # {4,5} 

  print(my_set.difference(your_set)) # {1,2,3} is like A - B
  print(my_set - your_set)

  # elements in the set and the iterable but not both
  print(my_set.symmetric_difference(your_set))
  print(my_set^your_set)

def set_mutation_operations():
  # ALL these operations changes original set 

  # update() or |= 
  my_set={1,2,3,4,5}
  your_set={4,5,6,7,8}
  print(my_set.update(your_set))
  print(my_set)
  print(your_set)

  # .intersection_update() or &=
  my_set={1,2,3,4,5}
  your_set={4,5,6,7,8}
  print(my_set.intersection_update(your_set))
  print(my_set)

  # .difference_update() or -=
  my_set={1,2,3,4,5}
  your_set={4,5,6,7,8}
  print(my_set.difference_update(your_set))
  print(my_set)

  # .symmetric_difference_update() or ^=
  my_set={1,2,3,4,5}
  your_set={4,5,6,7,8}
  print(my_set.symmetric_difference_update(your_set))
  print(my_set)

def set_is_operations():
  # ALL these operations changes original set
  my_set={1,2,3,4,5}
  your_set={4,5,6,7,8}
  print(my_set.isdisjoint(your_set)) # true if they have no common elements
  print(my_set.issubset(your_set))
  print(my_set.issuperset(your_set))
  
