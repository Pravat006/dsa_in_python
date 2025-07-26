# Hashmaps- Dictionaries
d= {
     'alok':1,
     'steve':2,
     'tony':3
 }

print(d)#{'alok': 1, 'steve': 2, 'tony': 3}

#Add key:val in dictionary: O(1)
d['rock']=4
print(d) #{'alok': 1, 'steve': 2, 'tony': 3, 'rock': 4}


#Ckeck for presence of key in dictionary: O(1)
if 'rock' in d:
    print(True)


#check the value corresponding to a key in the dictionary: O(1)
print(d['rock'])#4

# loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
    print(f'Key: {key}, Value: {val}')

# Defaultdict

from collections import defaultdict

default= defaultdict(list)
default[2]
print(default)  #defaultdict(<class 'list'>, {2: []})

#Counter
from collections import Counter

string= 'pravat'
counter= Counter(string)
print(counter) # Counter({'a': 2, 'p': 1, 'r': 1, 'v': 1, 't': 1})

