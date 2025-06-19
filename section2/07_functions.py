# parameters : when we use in definition 
def say_hello(name,emoji):
  print("Hello "+str(name)+' , '+str(emoji))

# called 'arguments' when we use it
# below are positional arguments
say_hello('lavnish',':)')
say_hello(':(','its morning')

# keyword arguments ... author says its bad practice
say_hello(emoji=':(',name='Lavnish')

def say_hello_with_defaults(name='John',emoji=':)'):
  print("Hello "+str(name)+' , '+str(emoji))

say_hello_with_defaults()
say_hello_with_defaults(name='Jilly')
say_hello_with_defaults('Jill') # without arg name
say_hello_with_defaults(emoji=':-|')

# NOTE : how to use return
def sum_three(num1,num2,num3):
  result=num1+num2+num3
  return result 

print('result is ='+str(sum_three(1,2,3)))
#####################
def first_functions(num1,num2):
  def embeded_functions(num1,num2):
    return num1+num2

def first_functions_1(num1,num2):
  def embeded_functions(num1,num2):
    return num1+num2
  return first_functions_1 # returns MEM location

def first_functions_2(num1,num2):
  def embeded_functions(num1,num2):
    return num1+num2
  return embeded_functions(num1,num2)

print('result is ='+str(first_functions_1(1,2)))
# NOTE : methods need a . before them , they are called in a context ... like "string".capitalize()
# functions dont need a context 

def say_hello_with_docstrings(name,emoji):
  '''
  This functions says hello with params
  '''
  # docstrings come as help text in editors
  print("Hello "+str(name)+' , '+str(emoji))
