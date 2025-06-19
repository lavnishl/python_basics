def multi_line_str():
  multi_line_str='''
    line#1
    line#2
  '''
  print('>>>'+multi_line_str+'<<<')

def string_escape_character():
  escaped_str_1='it\'s time to have fun'
  str_1='it\'s time to have fun'
  # print(escaped_str_1)
  # are both the strings equal ? 
  print('escaped_str_1 == str_1 = ?'+str(escaped_str_1==str_1))
  escaped_str_2="it\'s time to have more fun"
  # print(escaped_str_2)
  print('escaped_str_1==escaped_str_2 =? '+str(escaped_str_1==escaped_str_2))
  escaped_str_3="it\"s time to have max fun"
  # print(escaped_str_3)
  # will escaped_str_1 = escaped_str_2
  

string_escape_character()

def string_formatting():
  # old way : python 2
  print('Hi {} , glad to know you live in {}'.format('Johnny','Boston'))
  # new way : python 3  
  name='Jack'
  city='Tokyo'
  print(f'Hi {name} , glad to know you live in {city}')

def string_splicing_1():
  myStr = 'abcdefgh'
  #        01234567
  print(myStr[0:8])
  # start : end : stepover 
  print(myStr[0:8:1])
  print(myStr[0:8]==myStr[0:8:1])
  print(myStr[0:8] is myStr[0:8:1])


def string_splicing_2():
  myStr = 'abcdefgh'
  #        01234567
  print(myStr[::])
  print(myStr[0::])
  print(myStr[1::])
  print(myStr[:3:])
  print(myStr[::1])
  print(myStr[::-1])


def string_elements():
  myStr = 'abcdefgh'
  #        01234567
  print('str element at 0 : '+myStr[0])  
  print('str element at -1 : '+myStr[-1]) 
  print('str element at -2 : '+myStr[-2]) 

def strings_r_immutable():
  myStr = 'abcdefgh'
  # myStr[7]='x' # TypeError: 'str' object does not support item assignment
  print(myStr)
  myStr = 'newValue_NoError_str_can_be_fully_reassigned_but_not_partially_reassigned'
  print(myStr)

def str_methods():
  # 2ndStr = 'alpha beta gamma' # compile time error
  second_str = 'alpha beta gamma delta'
  #             0123456789

  print('second_str.Capitlaized = '+second_str.capitalize())

  print('str.upper. = '+second_str.upper()) # NOTE
  print('str.upper.lower = '+second_str.upper().lower())
  
  print('find(ta) '+str(second_str.find('ta')))
  print('second_str.replace() = '+second_str.replace('alpha','AAA'))


def str_functions():
  pass 
  # https://www.w3schools.com/python/python_ref_string.asp  

def multiple_display():
  print('a'*3)

