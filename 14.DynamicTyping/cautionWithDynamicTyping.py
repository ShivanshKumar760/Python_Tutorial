'''
Although Python is comfortable with changing types of a  variable , the programmer is responsible 
for ensuring right type for certain type of operation.For example;

X=10
Y=0
Y=X/2 # ------------->it is legal because two integer can be used in divide operation

X="Day"# ------>Python is comfortable with dynamic typing.

y=X/2 #------------->ERROR!a string cannot be divided.


----------------------------------------------------------------    

So as a programmer, we need to ensure that variable with right value should be usrd in expression.


If you want to determine the type of a varibale i.e, what type of value does it point to ?,we can use
type() in following manner:

    type(<varibale_name>)

For instance,consider the following sequence of commands that uses type() ----x3 times

a=10
print("a is :",a)
print(type(a))
a=20.5
print("a is :",a)
print(type(a))
a="hello"
print("a is :",a)
print(type(a))
'''


X=10
Y=0
Y=X/2 # ------------->it is legal because two integer can be used in divide operation

X="Day"# ------>Python is comfortable with dynamic typing.

y=X/2 #------------->ERROR!a string cannot be divided.