def lists_are_ordered():
  grocery_list = ['apple','bread','cinnamon','donuts']
  lists_can_contain_mixed_types = ['apple',1,True,None]
  # NOTE : index starts with 0
  print(grocery_list[0]==lists_can_contain_mixed_types[0])


def list_slicing():
  grocery_list = ['apple','bread','cinnamon','donuts']
  print('original grocery_list= '+str(grocery_list))
  print()
  new_list = grocery_list[1:3:1]
  print('[1:3:1]= '+str(new_list)) # >>NOTE<< 
  
  # lists are mutable
  grocery_list[0] = 'almonds'
  print(grocery_list)

  # >>NOTE<<  How is it different from above 
  grocery_list[0] = ['apricots']
  print(grocery_list)

def list_slicing_2():
  old_grocery_list = ['apple','bread','cinnamon','donuts']
  # grocery_list[0] = 'almonds'
  new_grocery_list = old_grocery_list
  new_grocery_list[0] = 'almonds'
  print(new_grocery_list)
  print(old_grocery_list) # ??? why ??? old  = new 
  # >>NOTE<<
  
def list_slicing_3():
  old_grocery_list = ['apple','bread','cinnamon','donuts']
  new_grocery_list = old_grocery_list[:]
  new_grocery_list[0] = 'almonds'
  print(new_grocery_list)
  print(old_grocery_list) 
  # >>NOTE<<


list_slicing_3()
# TODO : https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps
