num = int (input ("Input any num:")) #Any integer number
if num > 0:
    print ("Number is bigger zero")
elif num < 0:
    print ("Number is less zero")
else:
    print ("Number is zero")
del num
line = input ("Input any text:")
print ("Funny." if line == "any text" else "Ok.")