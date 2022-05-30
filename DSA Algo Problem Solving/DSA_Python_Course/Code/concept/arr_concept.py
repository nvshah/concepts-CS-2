import array

# int array
a1 = array.array('i', [1,2,3,4,5])
print(a1)

# double array
a2 = array.array('d', [1.2, 4.4, 5.4, 10.2])
print(a2)

# Methods ------
a = array.array('i', [1,2,3,4,5,6,7])
# 1. append()
a.append(8)
print(a)

# 2. insert()
a.insert(2, 10)
print(a)

# 3. extend()
a2 = array.array('i',[100, 200, 300])
a.extend(a2)
print(a)

# 4. fromlist()
l = [50, 60, 70]
a.fromlist(l)
print(a)

# 5. remove()
a.remove(200)
print(a)

# 6. pop()
e = a.pop()
print(a)

# 7 index()
i = a.index(7)
print(i)

# 8. reverse()
a.reverse()
print(a)

# 9. buffer info
print(a.buffer_info())

# 10. count()
a.append(6)
print(a.count(6)) # occurences

# 11. toString()
temp = a.tostring()
print(temp)
ia = array.array('i')  # int array
ia.fromstring(temp)
print(ia)

# 12.Slice
print(a[2:])


