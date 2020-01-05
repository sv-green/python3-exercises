from random import randrange

array_size = 20

array = [randrange (0,10000) for x in range (array_size)]

print ("Array:", array)

bubble = array.copy ()
flag = True
while flag:
    flag = False
    for i in range (array_size):
        if i < array_size - 1:
            if bubble[i] > bubble[i+1]:
                bubble[i],bubble[i+1] = bubble[i+1],bubble[i]
                flag = True

print ("Bubble", bubble)
