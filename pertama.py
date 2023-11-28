print("Hai")
print("selamat malam")

print("----NOT----")
a = True
b = not a
print("data Boolean = ", a)
print("------------------not")
print("data Boolean = ", b)


print("-----OR----")
a = False
b = False
print(a, "or", b, "adalah", a or b)
a = False
b = True
print(a, "or", b, "adalah", a or b)
a = True
b = False
print(a, "or", b, "adalah", a or b)
a = True
b = True
print(a, "or", b, "adalah", a or b)


print("-----XOR----")
a = False
b = False
print(a, "xor", b, "adalah", a ^ b)
a = False
b = True
print(a, "xor", b, "adalah", a ^ b)
a = True
b = False
print(a, "xor", b, "adalah", a ^ b)
a = True
b = True
print(a, "xor", b, "adalah", a ^ b)


print("-----AND----")
a = False
b = False
print(a, "and", b, "adalah", a and b)
a = False
b = True
print(a, "and", b, "adalah", a and b)
a = True
b = False
print(a, "and", b, "adalah", a and b)
a = True
b = True
print(a, "and", b, "adalah", a and b)
