l=["pratik", 1,2,3,2+2, "rohit sharma"]
print(l)

l.append("abhinandan")
print(l)

l.insert(2,"farate")
print(l)

l.pop(2)    #remove the last element or the given index elemet
print(l)

l.remove("abhinandan") #remove give value of element 
print(l)

print(l[0])

li=[1,2,7,8,4,2,57,7]
li.sort()
print(li)
li.extend([15,20,25,30])
print(li)

del li[0]
print(li)