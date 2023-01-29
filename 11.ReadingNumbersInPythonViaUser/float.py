'''
String value cannot be used for arithmetic or other numeric operations.For these operations we 
need to have values of numeric type (float ).

But what we would do if we have to read the numbers(float)?The function input() returns the 
entered value in string format only.Then what is the way out?

Don't worry .Python offers two function float() functions to be used with input() function
to convert the value received through input() into int and float types.We can :

    -> Read in the value using input() function
    ->And Then convert the value using float() functions with read value to change the type
    of input value to int or float respectively.

-------------------------------------------------------------------------------------------------------

        age = input("Enter the age:")
        print(type(age))#will print string data type
        #to convert it into float.
        age = float(age) # will convert age into float data type
        print(type(age)) # will print float data type
------------------------------------------------------------------------------------------------------

We can also combine these two steps in a single step too ie as:

<variable_name> = float(input(<prompt/info for user>))

--------------------------------------------------------------------------------------------------------

After using float() function with input() , we can check ourselves the type of value 
entered using type() function that the type of read value is now int or float now.

'''


age = input("Enter the age:")
print(type(age))#will print string data type
#to convert it into float.
age = float(age) # will convert age into float data type
print(type(age)) # will print float data type