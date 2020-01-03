variable01 = 10
variable02 = 3
variable03 = input ("Input any number: ")
variable04 = float (input ("Input float number: "))
variable05 = input ("Input some text: ")
sum_result = variable01 + int (variable03)
sub_result = variable02 - float (variable03)
dev_result = variable01 / variable02
mul_result = variable01 * variable04
txt_result = variable05 + variable05
sqr_result = int(variable03)
sqr_result *= sqr_result
print ("Sum is: ", sum_result)
print ("Substraction result is: ", sub_result)
print ("Division result is: ", dev_result)
print ("Multiplication result is: ", mul_result)
print ("Square " + variable03 + " is: ", sqr_result)
print ("Strings addition result is: ", txt_result)
print ("String multiplication result is", txt_result * variable02)
print ("Multiplication of two variables: ", sqr_result * dev_result)
del sqr_result
del txt_result