from random import randrange

array_size = 35

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

shaker = array.copy ()
flag = True
counter = 0

while flag:
    flag = False
    while counter < array_size -1:
        if shaker[counter] > shaker[counter + 1]:
            shaker[counter],shaker[counter +1] = shaker[counter +1],shaker[counter]
            flag = True
        counter += 1
    while counter > 0:
        if shaker[counter -1] > shaker[counter]:
            shaker[counter -1],shaker[counter] = shaker[counter],shaker[counter -1]
            flag = True
        counter -= 1

print ("Shaker", shaker)

print (bubble == shaker)