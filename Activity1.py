lst =['Apple','Guava','Mango','Banana','Kiwi']

print("Length of list:", len(lst))
print("First Element:",lst[0])
print("Last Element:",lst[-1])

lst.append('Papaya')
print("Update list", lst)

lst.remove('Guava')
print("Update list:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List:",lst)

lst.reverse()
print("Reversed :", lst)

print("Multiplication on List :",lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Updated List:", lst)