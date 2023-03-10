A = {1, 2, 3}
B = {4, 5, 6}

#union
print('Union using |:', A | B)
print()
print('Union using union():', A.union(B))

#intersection

print()
print('Intersection using &:', A & B)  #set()
C = {4, 5, 6}
D = {4, 5, 7}
print(C & D)

print()
#difference
E = {2, 3, 5}
F = {1, 2, 6}
print('Difference between A and B:', E - F)
print(E.difference(F))


#symmetric_difference
G = {2, 3, 5, 7}
H = {1, 2, 6, 7}
print('Symmetric Difference:', G ^ H )
print(G.symmetric_difference(H))

#equality
I = {1, 2, 3}
J = {1, 2, 4}
if I==J:
    print("set I and set J are equal")
else:
    print("set I and set J are not equal")
