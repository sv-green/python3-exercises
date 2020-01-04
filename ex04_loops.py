i = int (input ("Input num:"))
j = i
print ("Start point:", i)
while i < 100:
    if i == 0:
        break
    i += 1
else:
    print ("Zero not intersected.")
print ("End point:", i)
addidion = 0
ourrange = range(j) if j > 0 else range(j,0)
print (ourrange)
for counter in ourrange:
    if counter == 0:
        continue
    addidion += counter
print ("Result:", addidion)
