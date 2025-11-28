setOne = {1,2,3,4}
print(setOne & {1,3}) #Intersection of two sets
print(setOne | {1,3,5}) #Union of two sets
print(setOne - {1,2,3,4})
print(True + 4)

# Removing duplicates from list
# Ultimately list ko set bna do
l1 = [1,2,3,3,3,3,4,4,4,5,5,55,5,6,6,54,43,2,1,2,4]
s1 = set(l1)
print(s1)