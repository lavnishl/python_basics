def list_basics():
  #Ordered 
  #Form of an array
  #li = [1,2,’a’,true]
  # li[0] … starts with 0
  pass

def list_slicing():
  li=[1,2,3,4,5]
  new_list = li[1:3:1]
  print(new_list) # note : start & end & jump_count 
  pass

def list_slicing():
  li=[0,1,2,3,4,5,6,7,8]
  print(li[-1:8:1])
  print(li[-1:9:1])
  #print(li[0:9:2])
  #print(li[0:100:2]) # doesnt matter if end is > list size
  
def list_append():
  basket = [1,2,3,4,5]
  # append... changes the list in place, it doesn’t produce a value
  new_basket = basket.append(100);
  print(basket)
  print(new_basket)

def list_insert():
  basket = [1,2,3,4,5]
  new_basket = basket.insert(4,100);
  # i.e. the 4th element will be 100
  print(basket)
  print(new_basket)

def list_append_vs_extend():
  # append adds an element to a list, and extend concatenates the first list with another list (or another iterable, not necessarily a list.)
  
  # https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
  li = ['a', 'b', 'mpilgrim', 'z', 'example'] 
  print(li);
  #['a', 'b', 'mpilgrim', 'z', 'example']
  li.append("new") 
  print(li);
  # ['a', 'b', 'mpilgrim', 'z', 'example', 'new']
  li.append(["new", 2])
  print(li);
  #['a', 'b', 'mpilgrim', 'z', 'example', 'new', ['new', 2]]
  li.insert(2, "new")
  print(li);
  #['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', ['new', 2]]
  li.extend(["two", "elements"])
  print(li);
  #['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', ['new', 2], 'two', 'elements']

def list_pop():
  basket = [1,2,3,4,5]
  item = basket.pop();
  print(item);
  blank_list = []
  # item1 = blank_list.pop(); # indexError pop from empty list
  # print(item1);

def list_remove():
  basket = [1,2,3,4,5]
  item1 = basket.remove(2); 
  print(item1); # none
  print (basket);
  item2 = basket.remove(9) # ValueError : value not in list
  print(item2); 

def list_clear():
  basket = [1,2,3,4,5]
  basket.clear();
  print(basket);

def list_clear():
  basket = [1,2,3,4,5]
  basket.clear();
  print(basket); # []

def list_index():
  basket = [1,2,3,4,5]
  loc = basket.index(3,0,4);
  print(loc); # 2
  print(basket) # same as starting
  # loc1 = basket.index(7,0,4); # valueError 7 is not in list
  # if value not present ... do error handling OR use IN
  # print(loc1); 

def list_in():
  basket = [1,2,3,4,5]
  print(1 in basket)
  print(6 in basket)
  print('i' in 'Ian loves comedy') # false
  # NOTE : in operator never returns Error

def list_count():
  list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']  
  # Counts the number of times 'b' appears in list2 
  print(list2.count('b'))
  print(list2.count('B'))

  list3 = ['Cat', 'Bat', 'Sat', 'Cat', 'cat', 'Mat'] 
  # Counts the number of times 'Cat' appears in list3 
  print(list3.count('Cat')) 
  print(list3.count('CAT'))

def list_sort():
  basket = ['a','b','d','c','e']
  basket.sort() # modified original
  print(basket) # [‘a’,’b’,’c’,’d’,’e’]
  # basket.sort() vs sorted(basket)
  # first is a method , 2nd a function
  # First modifies the original , 2nd doesnt 
  # 2nd produces a new array 

def list_copy():
  basket = ['a','b','d','c','e']
  new_basket = basket.copy()
  basket[0]='A'
  print(basket) # see the changes 
  print(new_basket) # see original without changes
  basket2 = basket[:]
  basket[0]='Alpha'
  print(basket) # see the changes 
  print(basket2) # see original without changes

def list_reverse():
  basket = ['a','b','c','d','e']
  new_basket = basket.reverse()
  basket[0]='E'
  print(basket) # see the changes 
  print(new_basket) # None
  basket2 = basket[::-1]
  basket[0]='Alpha'
  print(basket) # see the changes 
  print(basket2) # see original without changes

def list_range():
  print(list(range(1,10))) # 1 … 9 
  print(list(range(10))) # 0 … 9
  # In Python 3.x ,range(0,3) returns a class of immutable iterable objects that lets you iterate over them
  
  # it does not produce lists, and they do not store all the elements in the range in memory, instead they produce the elements on the fly (as you are iterating over them) , 
  
  # whereas list(range(0,3)) produces a list (by iterating over all the elements and appending to the list internally) .
  ######
  print(range(0,10)[3:7]) # note = range(3,7)

def list_join():
  sentence=''
  print(sentence.join(['hi','my','name','is','lav'])) # does not modify original, returns new list
  print(sentence) # note no output

def list_unpacking():
  a,b,c, *other,d = [1,2,3,4,5,6,7]
  print(a)
  print(b)
  print(c)
  print(other) # [4,5,6]
  print(d) # 7

def list_slicing():
  pass
### LEFT , check in doc #### 