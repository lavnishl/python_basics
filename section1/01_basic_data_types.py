def basic_types_1():
  print ("2/4 ="+str(type(2/4)) ) # 0.5 = float 
  print ("0 = "+str(type(0))) # int
  print ("9.9+1.1 = "+str(type(9.9+1.1))) # float
  print(2 ** 3) # power
  print(3 // 4) # 0

def basic_types_default_values():
  i = int() # returns 0 
  print("i= "+str(i))
  f = float()
  print("f= "+str(f))
  s = str()
  print("s= "+str(s))
  b = bool()
  print("b= "+str(b))
  c = complex()
  print("c= "+str(c))
  s = set()
  # print("s= "+s) # TypeError can ONLY concatinate str to string
  print("s= "+str(s))

def misc_types():
  print("bin(5) : "+str(bin(5)))
  print("bin(5) : "+str(int('0b101',2))+" ,"+str(int('101',2))+" ,default base is 10 = "+str(int('0101')))
  # print("base must be >=2 or <=36 or 0 : "+str(int('101',-8)))

def operator_priority():
  pass
  # 1. ( )
  # 2. **
  # 3. * / 
  # 4. + -

def var_r_case_sensitive():
  i=10
  I=20
  print(i==I)

def operator_declare():
  a = b = c = d= 2
  print('a= '+str(a)+', b='+str(b))
  # https://stackoverflow.com/questions/27272034/what-is-a-b-c-in-python 
  x , y , z = 1 , 2 , 3
  print('x= '+str(x)+', y='+str(y)+', z='+str(z))

def compare_1():
  a = 1
  b = 2
  c = 3
  # https://stackoverflow.com/questions/18755059/is-abc-valid-python 
  '''
  https://docs.python.org/3/library/stdtypes.html
  There are eight comparison operations in Python. They all have the same priority (which is higher than that of the Boolean operations). Comparisons can be chained arbitrarily; for example, x < y <= z is EQUIVALENT TO x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).
  '''
  print('a<b<c = '+str(a<b<c)) # In bounds test
  print('not(b<a<c) = '+str(not(b<a<c))) # Out of bounds test
  print('not(a<c<b) = '+str(not(a<c<b))) # Out of bounds test

