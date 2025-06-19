print("paste your favorite code")
###########

###########
def for_loop_1():
  for iterable in 'Zero to Hero':
    print(iterable)
  ### same output ###
  #for iterable in " Zero to Hero":
  #  print(iterable)

  ### item is iterable ###
  # for iterable in [10,20,30,40,50]:
  #  print(iterable)

  ### SAME OUTPUT :  item is iterable ###
  #for iterable in (10,20,30,40,50):
  #  print(iterable)

  ### SAME OUTPUT : item is iterable ###
  for iterable in {10,20,30,40,50}:
    print(iterable) # NOTE : order will be different 

  print(iterable) # this will print last value of iterable

def nested_for_loop():
  for iterable1 in (10,20,30,40,50):
    for iterable2 in ('alpha','beta','gamma'):
      print('value is ['+str(iterable1)+','+str(iterable2)+']')

def iterable_map():
  # an iterable can be an element of set , list , tuple , dictionary
  # >> note keys must be immutable hence a string here , must use :
  stock = {
    'tickr' : 'tesla',
    'value' : 287
  }
  print('>>> map iterbale <<<')
  for iterable in stock:
    print(iterable)
  print('>>> keys iterbale <<<')  
  for iterable in stock.keys():
    print(iterable)
  print('>>> value iterbale <<<')
  for iterable in stock.values():
    print(iterable)
  print('>>> items iterbale <<<')
  for iterable in stock.items():
    print(iterable) # NOTE : you get tuples here
  print('>>> items iterbale again <<<')
  for iterable in stock.items():
    key , value = iterable # NOTE * SYNTAX * 
    print('key='+str(key),',value='+str(value)) 
  ##### TODO 05:20 from video#67###

def non_iterable_int():
  for iterable in 21:
    print(iterable) # TypeError: 'int' object is not iterable

def counter_function():
  count=0
  for iterable in (1,2,3,4,5,6,7):
    print(iterable)
    count=count+1
  print('Number of elements in list is'+str(count))

