# https://towardsdatascience.com/python-eval-built-in-function-601f87db191

input = input("Enter any number of your choice:")
print(input)
print(type(input))
#######################
#Enter any number of your choice: 10 + 10 
#10 + 10 
#<class 'str'>

eval = eval(input("Enter any number of your choice"))
print(eval)
print(type(eval))
#######################
#Enter any number of your choice: 10 + 10 
#20 
#<class 'int'>
###########################
x = 1
eval('x+1')
#2
##########################
print(type(eval(input("enter value"))))
# if yu enter 10 you get int 
# if you enter 10.0 you get float 
# if you enter list [1,2] LIST
##################
# 4. Can we perform mathematical operations using eval function
evaluate = input("Enter what operation x has to perform: ")
print(evaluate)
print(type(evaluate))
##############
#Enter what operation x has to perform: x + x + 100 - 35 + 5 * 80 
#x + x + 100 - 35 + 5 * 80 
#<class 'str'>
x = 10
print(type(x))
##################
# <class 'int'>
expression = eval(evaluate)
print(expression)
print(type(expression))
###############
485 
# <class 'int'>


### below is GOOD 
# https://www.programiz.com/python-programming/methods/built-in/eval 