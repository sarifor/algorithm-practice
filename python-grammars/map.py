# for statement
a = [1.2, 2.5, 3.7, 4.6] # list
for i in range(len(a)):
    a[i] = int(a[i])
print(a) # [1, 2, 3, 4]


# map function (simpler)
b = [1.2, 2.5, 3.7, 4.6] # list
b = list(map(int, a))
print(b) # [1, 2, 3, 4]

c = list(map(str, range(10))) # iterable besides list
print(c) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# input().split() and map
d = input().split() # Input 10 20
print(d) # ['10', '20'] (input().split() returns list)

e = map(int, input().split()) # Input 10 20
print(e) # <map object at 0x0000017AACB6BFA0>
print(list(e)) # [10, 20]


# Save list into two variables
f, g = [10, 20]
print(f) # 10
print(g) # 20

h, i = map(int, input().split()) # Input 10 20
print(h) # 10
print(i) # 20

j = input().split() # Input 10 20
k = map(int, j)
l, m = k # map object is iterator so it can be unpackaged into more than one variable, which means list(k) can be omitted.
print(l) # 10
print(m) # 20