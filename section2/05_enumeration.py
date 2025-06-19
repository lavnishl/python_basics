def enumeration_use_1():
  
  # we have to give something that enumerate can go over
  for iterable in enumerate("abcd"):
    print(iterable) # will attache index to value
  print("**** gives index and value for string *****")
  for index,iterable in enumerate("abcd"): # we are unpacking this
    print(index,iterable) # will attache index to value
  print("**** gives index and value for TUPLE *****")
  for index,iterable in enumerate((10,20,30,40)): 
    print(index,iterable) 
  print("**** list of range *****")
  for index,iterable in enumerate(list(range(10))): 
    if(iterable==5):
      print('Number 5 is at location '+str(index))     
  # NOTE : enumerate takes MAX of 2 args

enumeration_use_1()