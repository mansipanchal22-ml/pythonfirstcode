#Q.1 Type Casting Constructors (int(), float(), str(), bool())

value = input("Enter a value: ")

print("Original Value:", value, type(value))

try:
    int_value = int(value)
    print("Integer:", int_value, type(int_value))
except:
    print("Cannot convert to Integer")

try:
    float_value = float(value)
    print("Float:", float_value, type(float_value))
except:
    print("Cannot convert to Float")

str_value = str(value)
print("String:", str_value, type(str_value))

bool_value = bool(value)
print("Boolean:", bool_value, type(bool_value))