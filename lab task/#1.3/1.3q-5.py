# Q.5 memory address using id()

a = 50
b = 50

print("Initial Values")
print("a =", a, "Memory Address =", id(a))
print("b =", b, "Memory Address =", id(b))

if id(a) == id(b):
    print("Both memory addresses are same.")
else:
    print("Memory addresses are different.")

b = 100

print("\nAfter modifying b")

print("a =", a, "Memory Address =", id(a))
print("b =", b, "Memory Address =", id(b))

if id(a) == id(b):
    print("Both memory addresses are same.")
else:
    print("Memory addresses are different.")