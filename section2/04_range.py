def use_range():
  # returns an object that produces a sequence from start to stop
  # its not tuple , its a special type of object
  print("range object = "+str(range(100))) # note 
  print("range object = "+str(range(90,100))) # note : 100 is not part of range ... starts with 90...
  my_range1 = range(90,100,2)
  for iterator in my_range1:
    print(iterator)
  # can use _ in place of variables you dont care
  _ = range(90,100)
  for iterator in my_range1:
    print('in range')
    my_range1 = range(90,100,2)
  # Note will below work ? 
  for _ in range(0,10,-1):
    print('-ve iterator')
  # will below work ?
  for _ in range(10,0,-1):
    print('opposite count '+str(_))

  for _ in range(10,0,-5):
    print(list(range(10)))


# call your favorite method here
use_range()