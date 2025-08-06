lst= [1,2,3,4,5]
if lst == []:
    print("lst is empty")
else:
    lst.insert(0, lst.pop())
print(lst)
