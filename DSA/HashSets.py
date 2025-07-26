# Hashsets
s= set()
print(s)

# add item into set - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s) #{1, 2, 3}

# Lookup if item in set - O(1)

if 1 not in s:
    print(True)

# Remove item fom set - O(1)

s.remove(1)
print(s) #{2, 3}

#set construction -O(S) - S is the length of the string
string= 'aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccceeeeeeeeedddddddd'
# print(string.split()) #['aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccceeeeeeeeedddddddd']
sett = set(string)
print(sett) #{'c', 'e', 'b', 'a', 'd'}

#Loop over items in set - O(n)
for x in s:
    print(x)



