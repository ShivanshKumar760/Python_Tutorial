"""
Python is very versatile with assignments.Lets see in how many different ways , we can use assignments in 
Python:

1.Assigning same value to multiple variables:
----------------------------------------------
We can assign same value to multiple variables in a single statement.e.g:
a=b=c=10

it will assign the same value 10 to all three variables a,b,c.That is ,all three label a,b,c will refer to same 
location with value 10.
------------------------------------------------------------------------------------------------------------------

2.Assigning Multiple Value to multiple variables
-------------------------------------------------
We can assign multiple values to multiple variables in single statement,e.g:
x,y,z=10,20,30
it will assign the values order wise ie first variable is given first value , second variable the second value
and so on.That means above statements will assign value 10 to x , 20 to y , 30 to z.

This style of assigning values is very helpful when and useful plus compact.For example,consider the code
below:

x,y=25,50
print(x,y)

will print:
25 50

"""

print("""
1.Assigning same value to multiple variables:
----------------------------------------------
We can assign same value to multiple variables in a single statement.e.g:
a=b=c=10

it will assign the same value 10 to all three variables a,b,c.That is ,all three label a,b,c will refer to same 
location with value 10.

""")

a=b=c=10
print("a,b,c",a,b,c)
print("------------------------------------------------------------------------------------------------------------------")

print("""
2.Assigning Multiple Value to multiple variables
-------------------------------------------------
We can assign multiple values to multiple variables in single statement,e.g:
x,y,z=10,20,30
it will assign the values order wise ie first variable is given first value , second variable the second value
and so on.That means above statements will assign value 10 to x , 20 to y , 30 to z.

This style of assigning values is very helpful when and useful plus compact.For example,consider the code
below:

x,y=25,50
print(x,y)

will print:
25 50
""")

x,y=25,50

print(x,y)
print("------------------------------------------------------------------------------------------------------------------")
