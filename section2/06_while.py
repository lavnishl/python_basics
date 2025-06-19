def while_basic_example():
  i=0
  while(i<50):
    i+=1
    if(i==10):
      break
  else: # ** NOTE ** 
      print("else is reached when while loop is done")
  print("exit value of i="+str(i))

# break can be used in while and for both 

# continue : continues loop 

# pass : just passes to next line 
def pass_example():
  some_list=[1,2,34]
  for iterator in some_list: 
    pass
  print("finished pass")

def print_without_newline():
  for _ in (1,2,3):
    print("*",end="")

# array has a count function
def find_duplicate():
  my_list=['a','b','c','a','d','e','b','f']
  duplicates=[]
  for value in my_list:
    if my_list.count(value) > 1:
        if value not in duplicates:
          print ('duplicate found '+str(value))
          duplicates.append(value)
      

find_duplicate()