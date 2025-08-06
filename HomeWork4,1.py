lst = [2, 0, 4, 0, 0, 7, 11, 0, -2, 8]
x = lst.count(0)
for i in range(x):
    lst.remove(0)
lst.extend([0] * x)
print(lst)
