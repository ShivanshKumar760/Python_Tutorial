'''
String value cannot be used for arithmetic or other numeric operations.For these operations we 
need to have values of numeric type (integer).

But what we would do if we have to read the numbers(int)?The function input() returns the 
entered value in string format only.Then what is the way out?

Don't worry .Python offers two function int() functions to be used with input() function
to convert the value received through input() into int  types.We can :

    -> Read in the value using input() function
    ->And Then convert the value using int() functions with read value to change the type
    of input value to int or float respectively.


    Example:
        age = input("Enter the age:")
        print(type(age))#will print string data type.
        #to covert it into a int.
        age = int(age) # will convert age into int data type.

        print(type(age))#will print int data type
---------------------------------------------------------------------------------------------------


We can also combine these two steps in a single step too ie as:

<variable_name> = int(input(<prompt/info for user>))


--------------------------------------------------------------------------------------------------------

After using int() function with input() , we can check ourselves the type of value 
entered using type() function that the type of read value is now int or float now.
'''

age = input("Enter the age:")
print(type(age))#will print string data type.
#to covert it into a int.
age = int(age) # will convert age into int data type.
print(type(age))#will print int data type