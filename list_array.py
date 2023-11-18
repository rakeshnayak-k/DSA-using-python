import array as array

# array in python
a1 = array.array('i',[1,2,3])

print(type(a1))
print(a1)

a1.append(4)
a1.insert(0,2)

print(a1)
for i in a1:
    print(i)


# list

l = [1,3,'e','',9.0,None]
for i in l:
    print(i)
l.insert(0,0)
a = l.pop()
print(l)
l.append(a)
print(l)
