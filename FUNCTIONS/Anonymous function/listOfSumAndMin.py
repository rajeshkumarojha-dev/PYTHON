
def max(lst):
    maxv = lst[0]
    for val in lst:
        if(val>maxv):
            maxv = val
    return maxv

def min(lst):
    minv = lst[0]
    for val in lst:
        if(val<minv):
            minv = val
    return minv


findMax = lambda lst: max(lst)
findMin = lambda lst: min(lst)
print("Enter numbers: ")
lst = [ int(val) for val in input().split()]
print("List of value is :{}".format(lst))
bigv = findMax(lst)
smv = findMin(lst)
print("maximum value is : {}".format(bigv))
print("manimum value is : {}".format(smv))