# # Tuples are immutable, initialized with ()
# waffle = ("Shubham", "Rajan", "Rane");
# print(waffle.index("Shubham"));
# # print(waffle.index("Shubham",1)); # This one throws an error
# print( len(waffle) );

# Unpacking with Tuples
coordinates = (40.6474, -73.02765, 238);
x, y, z = coordinates;
print(x, y, z);
print(coordinates);

# Packing with Tuples
x = -40.8583724;
y = 73.4758347;
z = 238;
coordinates = x,y,z;
print(coordinates);
