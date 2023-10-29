numbers = [5,2,5,2,2];

# Approch 1:
for number in numbers:
    print( "x" * number);

print("*****************************");

# Approch 2:
for number in numbers:
    output = "";
    for x_count in range(number):
        output += "x";
    print(output)