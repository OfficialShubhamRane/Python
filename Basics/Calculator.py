print("Type from following operations: ");
print("add, sub, mul, div, power, mod");

operation = input();
num_1 = input("Number 1: ");
num_2 = input("Number 2: ");


if operation == "add":
    print( str( float(num_1) + float(num_2)));
elif operation == "sub":
    print(str(float(num_1) - float(num_2)));
elif operation == "mul":
    print(str(float(num_1) * float(num_2)));
elif operation == "power":
    print(str(float(num_1) ** float(num_2)));
elif operation == "div":
    print(str(float(num_1) / float(num_2)));
elif operation == "power":
    print(str(float(num_1) % float(num_2)));
else:
    print("Wrong input");