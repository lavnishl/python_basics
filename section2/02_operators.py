print("paste your favorite code")
###########

###########
def ternary_operator():
  is_friend = False
  can_message = "message allowed" if is_friend else "not allowed to message"
  print(can_message)

##### Short Circuiting ######
def short_circuit():
  is_friend = True
  is_User = True
  if is_friend or is_User: # or is short circuting , hence BETTER performance
    print("best friends forever")
  else:
    print("not best friends")

#### Logical Operator ####
def Logical_Operator():
  # print(4=5) # Syntax error : keyword cant be an expression 
  print(4==5) 
  print('a'>'A')
  print(1<2<3<4)
  print(1>=0)
  print(0!=0)
  print(1!=0)
  # and , or , not 
  print(not(True))

def Logical_Operator2():
  is_magician = False
  is_expert=True
  if(is_expert and is_magician):
    print("you are master magician")
  elif is_expert or is_magician: # its not clear if expert but if not magician 
  # elif is_expert and not is_magician: # this makes it clear 
    print("at least you are getting there")  

def bool_basics():

  print('blank string ='+str(bool('')))    # false
  print('zero ='+str(bool(0)))     # false

  print('one ='+str(bool(1)))     # true

  print('array empty string ='+str(bool('[]'))) # true
  print('array non-empty string ='+str(bool('[1]'))) # true

  print('ten ='+str(bool(10)))    # true
  print('ten.o ='+str(bool(10.0)))  # true
  print('a ='+str(bool('a')))   # true
  print('1 string ='+str(bool('1')))   # true

def double_equal():
  # is vs == video#65: == compares value, is compares memory
  print('True == 1 =>'+str(True == 1))
  print("'' == 1 =>"+str('' == 1))
  print("'1' == 1 =>"+str('1' == 1))
  print('[] == 1 =>'+str([] == 1))
  print('10 == 10.0 => '+str(10 == 10.0 ))
  print('[] == [] =>'+str([] == [] ))
  print('[1,2,3] == [1,2,3] =>'+str([1,2,3] == [1,2,3] ))

def is_operator():
  # is : checks if the memory location is same 
  print('True is 1 =>'+str(True is 1))
  print("'' is 1 =>"+str('' is 1))
  print("'1' is 1 =>"+str('1' is 1))
  print('[] is 1 =>'+str([] is 1))
  print('10 is 10.0 => '+str(10 is 10.0 ))
  print('[] is [] =>'+str([] is [] ))
  print('[1,2,3] is [1,2,3] =>'+str([1,2,3] is [1,2,3] ))


def is_operator_2():
  # is : checks if the memory location is same 
  print('True is True = '+str(True is True))
  print('blank str is blank str = '+str('' is ''))
  print('one str is one str = '+str('1' is '1'))
  print('one int is one int = '+str(1 is 1))
  print('ten int is ten int = '+str(10 is 10 ))
  print('blank array is blank array = '+str([] is [] )) # coz both are in different MEMORY location
  print('filled array is filled array ='+str([1,2,3] is [1,2,3] ))

# call your method
is_operator_2()