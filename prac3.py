mylist = [1, 34, 5, 23, 21, 11]
mylist2 = [32, 21, 12, 34, 41, 2, 34]
mylist.sort()
mylist2.sort()
newlist=[]
for x in mylist:
    if x in mylist2:
        newlist.append(x)
print(newlist)
