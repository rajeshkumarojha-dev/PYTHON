def asc(names):
    ascending = sorted(names)
    return ascending

def desc(names):
    names.sort(reverse = True)
    return names

findAsc = lambda names: asc(names)
findDesc = lambda names: desc(names)

print("Enter multiple names: ")
names = [ val for val in input().lower().split()]

ascending_names = findAsc(names)
decending_names = findDesc(names)
print("-"*50)
print("List of Acending value : {}".format(ascending_names))
print("-"*50)
print("List of Decending value : {}".format(decending_names))
print("-"*50)




