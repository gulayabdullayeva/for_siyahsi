#siyahlar ve ya list tipi

numeber = 5,6
print(type(numeber))
words = "alpha"
print(type(words))
list1 =[]
print(type(list1))


lst1 =[2,-5,6 , "alma", -6, 13]
letters = "abcd"
print(letters[2])
print(lst1[2])

# siyahi metodlari
#1. append (elemet)- siyahinin sonuna yeni element elave edir
lst1.append(19)
lst1.append(2.5)
print(lst1)

# 2. insert (index, element) - siyahinin istediyimiz indexine yeni element elave edir
lst1.insert(2, 70)
lst1.insert(4,100)
print(lst1)

# 3.extend (list) - siyahinin sonuna yeni siyahi elave edir
a = [1,2,3]
b = [4,5,6]
#a.extend(b)
#print(a)
a.extend(b)
print(a)

# 4. remove (element) - siyahidan istediyimiz elementi silir
a. append(5)
a.remove(5)
print(a)

# 5. pop (index) - siyahidan istediyimiz indexdeki elementi silir
c = [10,20,30,40]
c.pop(1)
print(c)

# 6. clear() - siyahinin butun elementlerini silir
# c.clear()
# print(c)

# 7. count() - siyahida istediyimiz elementin nece defe oldugunu yoxlayir
d = [1,2,3,4,5]
print(d.count(2))

# 8. del() - siyahidan istediyimiz indexdeki elementi silir
#del(c)
#print(c)

# 9. sort() - siyahini kicikden boyuye siralayir
d.sort()
print(d)

#10. reverse() - siyahini tersine cevirir
d.reverse()
print(d)

