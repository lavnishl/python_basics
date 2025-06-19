def many_postional_args(*someVar):
  print(*someVar)
  return(sum(someVar))

print(many_postional_args(1,2,3,4))

def many_postional_args_2(*someVar,**keyValueArgs):
  print(*someVar)
  print(*keyValueArgs)
  total=0
  for items in keyValueArgs.values():
    total += items
  return total + sum(args)

print('Sum of KV='+str(many_postional_args_2(1,2,3,4,num1=2,num2=5)))


