# The Basics
is_old=False
is_licensed=True
if is_old: # note the : , can use 'and' 'or' etc.
  print ("old enuf to drive")
elif is_licensed: # note the :
  print ("drive safely")
# elif <more_condition>
else :
  print ("too young")
  print ("choose a good driving school")


# Type Conversion for boolean  
bool_val=True
num_as_bool=5
if bool_val and num_as_bool :
  print ("number treated as true") 
else:
  print ("number NOT treated as true")
print("Truthy is="+str(bool(5))) # truthy values in pthon


# More Truthy...
password='secret'
username='myname'
if password and username:
  print("thank you for giving username and password")
else:
  print("please provide username and password")

print("end of program")