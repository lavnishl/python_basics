var = 1

def sample_function():
  var = 7
  def embeded_function():
      return var
  print('value inside ='+str(embeded_function()))

print(var)
print(sample_function())

# 1 : start with local scope 
# 2 : is there a parent scope
# 3 : global scope 
# 4 : built in python 

total=0
def global_count():
  global total
  total += 1
  return total

global_count()
print("global count ="+str(global_count()))

############ non local ##########
# non local is a way to refer parent variable
def outer():
 x = "local"
 def inner():
  nonlocal x # comment this and check output
  x = "nonlocal"
  print("inner: "+x)
 inner()
 print("outer =",x) # NOTE 

outer()