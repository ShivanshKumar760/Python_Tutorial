'''
(iii)The id of an object :

The id of an object is generally the memory location of the object.Although (id) is implementation dependent but in most implementations
it returns the memory location of the object,Built-in functions id() returns the id of an object,e.g.,

a=4
print(id(4))# will return the memory location of the integer value 4
print(id(a))#will return the referencing memory location of the a which is same as integer value 4
'''

a=4
print(id(4))# will return the memory location of the integer value 4
print(id(a))#will return the referencing memory location of the a which is same as integer value 4