# Let's create an object called "a" and assign it the number 5
a = 5
print("a =", a)

# Adding the objects
print("a+a =", a+a)

# Reassignment
a = 10
print("a =", a)

# Use A to redefine A
a = a + a
print("a =", a)

a += 10
print("a =", a)

# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

# Show my taxes!
print("my_taxes =", my_taxes)

# dynamic typing
print("Dynamic Typing")
my_dogs = 2
print("my_dogs =", my_dogs)
print("type of my_dogs =", type(my_dogs))

my_dogs = ['Sammy', 'Frankie']
print("my_dogs =", my_dogs)
print("type of my_dogs =", type(my_dogs))

my_dogs = (1,2) # tuple
print("my_dogs =", my_dogs)
print("type of my_dogs =", type(my_dogs))
