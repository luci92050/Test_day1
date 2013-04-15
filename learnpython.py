### change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print "String: %s" % mystring
if isinstance(myfloat, float) and myfloat == 10.0:
    print "Float: %d" % myfloat
if isinstance(myint, int) and myint == 20:
    print "Integer: %d" % myint

ex2:

######
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append('world')

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
#########

