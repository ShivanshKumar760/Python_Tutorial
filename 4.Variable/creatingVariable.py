"""
in order to create a variable in python we just need to select a variable name and assign a value to it

unlike other programming languages where we need to specify variable data type and then give a variable name like

int a;
a=4;

or char c;
c='d';


in python we dont need to specify a data type to variable name we just have to asssign a value to variable name
and python interpreters is smart enough to determine the data type of a variable.

Now how to create a variable name :-

rules to create a variable name are :-
PYTHON IDENTIFIER
--------------------
a)Python identifier refer to a name used to identify a variable,function,module ,class or other objects

b)a identifier name should start with a alphabetic character(a-z)or(A-Z) or underscore character

c)a variable name or identifier name should not start with a number

d)special characters should not be included in identifiers

e)identifier name are case sensitive ie xyz is not same as XYZ


valid python identifier name :
number
number_1
_a
invalid identifier name:
7number 
_@num2

"""

number = 2#and we know that 2 is a whole number with no decimal point so a will pe integer type and we can check that via type()
print(type(number))
#this will output "number " as integer type and with that we can say we have created a variable name number without pre definig its data type thats how easy it is in python to declare a variable