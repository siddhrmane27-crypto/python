tup=("shiva","shiva 1","shiva 2","shiva 3","shiva 4")
tup2=list(tup)
print(tup2)

tup2[4]="shiva 5"

print(tup2)

print(type(tup2))

tup2.append("shiva 6")

print(tup2)

tup=tuple(tup2)
print(tup)

(s1,s2,s3,s4,s5,s6)=tup
print(s1)
print(s2)
print(s3)

