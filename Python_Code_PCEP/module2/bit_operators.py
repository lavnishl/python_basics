#temp-one=100 # error before running
#print(temp-one) 

# &
first_bit = 1
second_bit = 0
third_bit = 1

print("one ",first_bit & second_bit) # 0
print("two ",second_bit & first_bit) # 0
print("third ",second_bit & first_bit & third_bit) # 0
print("fourth ",first_bit & first_bit & first_bit) 

first_number = 4 # 0100
second_number = 5 # 0101
print("five ",first_number & second_number) # 0100 = 4

first_decimal = 4.5
second_decimal = 5.5
#print("six ",first_decimal & second_decimal) # error float not supported for bitwise operation

# |

# ^

# ~ : only one with single operand (or input)
print("not one ",~first_number)

# << 
x = -7
print("shift left 1",x << 1)
print("shift left 2",x << 2)

# >>
y = 140
print("shift right 1",y >> 1)
print("shift right 2",y >> 2)
print("shift right -1",y >> -1) # runtime error .... ValueError: negative shift count
