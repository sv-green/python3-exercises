lst = [] #Blank list
print ("Blank list:", lst)
lst.append (10) #Adds a one item at the end of list.
lst.append ('A')
lst.insert (0,5) #Inserts a new item in place with a zero index.
print ("List has three elements", lst)
tmp = ['D','F',-2.5, 'V']
lst.extend(tmp) #Extends the list with the values of another list.
del tmp
print ("List got a items from another list", lst)
tmp = ['G',12,'V','7',"R45"] 
lst.insert (2,tmp) #Inserts a other list as a item of current.
print ("List has a new list as a item", lst)
lst += ["A", 'V', 10] #Merges a two lists.
del tmp
print ("List got a items from another list", lst)
print ("Index:", lst.index ('A')) #Returns the index of the first item found.
print ("Count:", lst.count ('V')) #Returns a count of items.
lst.pop (2)
print ("Removed item with index 2:", lst)
lst.remove ('A')
print ("Removed first item 'A'", lst)
lst.clear ()
print ("Cleared list", lst)
lst = [10,2,19,3.2,7,90,2.5,17.2,92,55,1,24,-7,0.3,-34]
print (lst)
lst.sort ()
print (lst)
lst.reverse ()
print (lst)
lst.clear ()
lst = [x * y for x in range(10) if x > 0 for y in range(-10,10) if y != 0]
#lst.sort ()
print (lst)