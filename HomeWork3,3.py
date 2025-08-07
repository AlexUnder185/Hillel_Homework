lst = [2, 4, 7, 11, 0, -2, 8]
length = len(lst)
middle = (length + 1) // 2

lst1 = lst[:middle]
lst2 = lst[middle:]
if length == 0:
    print([[], []])
else:
    print(lst1)
    print(lst2)
