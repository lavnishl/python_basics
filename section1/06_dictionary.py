def dict_basic():
  # HashMap = un ordered key value pair
  dictionary = {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True,
    '123' : [4,5,6]
  }
  print(dictionary['a'][1]) #2
  print(dictionary['123'][1]) #5
  pass

def list_of_dict():
  my_list_of_dict=[
    {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
    },
    {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
    }
  ]
  print(my_list_of_dict[0]['a'][1]) #2

def dict_key_attributes():
  # (1) Dictionary Key cannot be of type list
  # (as its un hashable, it can be string, integer, EVEN boolean) 
  
  # (2) Key cannot be mutable , needs to be immutable
  
  # (3) Has to be unique … else the last value is picked
  pass

def how_to_access_map_value_without_error():
  dict = {'Name': 'Zabra', 'Age': 7}
  print (dict.get('Age'))
  print (dict.get('Education', "Never"))
  # print(dict['Education']) # KeyError
  ### anti pattern below #### 
  data = ""
  if 'Education' in dict:
    data = dict['Education']
  print(data)  # blank coz it doesnt exists
  
def getting_keys_from_map():
  map = {'Name': 'Zabra', 'Age': 7}
  print('Name' in map) # will print true or false
  print('name' in map.keys()) 
  print('key1' in map.values()) 
  print('key1' in map.items()) # returns a tuple

def dict_misc():
  # clear
  map = {'Name': 'Zabra', 'Age': 7}
  map.clear()
  print(map)
  # copy 
  map = {'Name': 'John', 'Age': 9}
  map2 = map.copy()
  print(map2)
  print(map2.pop('Age'))
  # print(map2.pop('age')) # KeyError
  print(map2.popitem()) # returns arbitrary tuple

def dict_updates():
   map = {'Name': 'Zabra', 'Age': 7}
   map.update({'Name':'John'}) #updates value 4 key , note :
   print(map)
   map.update({'name':'John'}) # updates value 4 key , note :
   print(map) # note 

dict_updates()