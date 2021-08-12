# Lists
lists = ["Ati", "Bhup", "Deep", "Sun", 5, ["Text", "List"]]

print(lists)
print(type(lists[4]))
print(type(lists[5]))
print(type(lists[5][0]))
print(lists[-1])
print(lists[1:])
print(lists[1:3])
print(lists[:3])
print(lists[:])

lists[5] = "New Str"
print(type(lists[5]))
print(lists)
