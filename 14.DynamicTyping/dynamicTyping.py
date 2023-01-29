'''
In Python,as we have learnt a variable is defined by assigning to it some value(of a particular type
such as numeric,string etc.)

for instance,the statement:
    x=10
we can say that variable x is reffering to a value of integer type.

Later in our program,if we reassign a value of some other type to variable x,python will not complain
(no error will be raised),e.g,

    x=10
    print(x)
    x="Hello, world!"
    print(x)

Above code will yeild the output as :
    10
    Hello, world
So,you think of a Python variable as labels associated with objects(literal valuesin our case here);
with dynamic typing ,python makes the label refer to new value.



 --------------------------------------------------
|A variable pointing to a value of a certain type,|
|can be made to point to a value/object           |
|of different type.This is called dynamic typing. |
---------------------------------------------------




x=10      [x]---------->Int:10
.
.
.
x="Hello, world!"  [x]----break---->Int:10
                    \
                     \
                      \
                       \String:Hello, world

As we can see in figure ,varibale x is first pointing to /reffering to an integer value 10 and then
to a string value "Hello, world!"


Please note here that variable x does not have a type but the value its pointing to does have a type.
So we can make a variable point to a value of different type by reassigning a value of that type;
Python will not raise an error.This is called DYNAMIC TYPING feature of python.


'''

x=10
print(x)
print(type(x))
x="Hello, world!"
print(x)
print(type(x))