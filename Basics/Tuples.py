# Tuples are immutable, initialized with ()
waffle = ("Shubham", "Rajan", "Rane");
print(waffle.index("Shubha/m"));
# print(waffle.index("Shubham",1)); # This one throws an error
print( len(waffle) );

# Unpacking wit Tuples
coordinates = (40.6474, -73.02765, 238)
x, y, z = coordinates
print(x, y, z);