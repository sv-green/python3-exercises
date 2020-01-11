lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K"]
print ("Complete list:", lst)
print ("Index = 1:", lst[1])
print ("Index = -1:", lst[-1])
print ("Slice = 2-4", lst[2:4])
print ("Slice = Begining-3", lst[:4])
print ("Slice = 5-End", lst[5:])
print ("Slice with step 2:", lst[::2])

for counter in lst:
    print (counter)

counter = lst.__len__()
while counter > 0:
    counter -= 1
    print (lst[counter])
    