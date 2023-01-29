"""
Output through print statement :
----------------------------------

The print() function of python 3.x is a way to send output to standard output device ,which is normally monitor

The simplified syntax of print() function is followed as :

print(*object,[sep=''or <seprator-string>end='/n' or <end-string> ])

*object means it can be one or multiple comma separated objects to be peinted.

let us consider the following examples;
print("hello") #prints a string
print(17) #prints a number or int 
print(17.5) #prints a number or float


print(3.14159*(r*r)) #the result of a calculation ,which will be performed by Python and then printed out(assuming number has been assigned to variable r)


print("I\'m",12+5,"years old.")
#multiple comma seprated expressions 

NOTE: A print() without any value or name or expression prints a bank line


"""

#Consider some examples:
print("---------------------------------------------------------------")
print("Python is wonderful")#will print : Python is wonderful

print("Sum of 2 and 3 is ",2+3) # will print the output as follow  (2+3 is evaluated ans its result is printed as 5 ): Sum of 2 and 3 is 5

a=25 
print("Double of",a,"is",a*2)
"""
will print the output as follows(a*2 is evaluated ans its result is printed as):

Double of 25 is 50
"""

"""
FEATURES OF PRINT STATEMENT:
-----------------------------

1.)It converts the item to a string ie if we are printing a numeric value ,it will be converted automatically to
string and print it;for numeric expressions ,it first evaluates them and then converts the result to string and print it
as done in statement 2 above ie print("Sum of 2 and 3 is ",2+3)

2.)it inserts space between item automatically because the default value of sep argument is space(" ").The sep argument
specifies the separator character between parameters separated by comma .The print automatially adds the 
separator character between parameters and item/objects being printed in a line .If we do not give any value for sep,
then by default the print() will add a space between parameters when printing .Consider this code:

print("My","name","is","Shivansh")

will print
My name is Shivansh //as we can see the output line has automatically inserted space between parameters when printed.


We can change the value of seprator character with sep argument of print() as per this :

the code:
print("My","name","is","Shivansh",sep="...")

will print :
My...name...is...Shivansh <------this time the print() seprated the item with given sep character,which is "..."

"""
print("-------------------------------------")
print("My","name","is","Shivansh")
print("My","name","is","Shivansh",sep="...")

"""
3.)it appends a new line character at the end of the line unless we give our own (end) argument.Consider the code given below:

print("My name is Shivansh")
print("I am 19 years old")


will print :
My name is Shivansh----after printing this line automatically changed given a \n character which means change line
I am 19 years old

The print() works this way only when we have not specified any (end) argument with it because by default print()
takes value for end argument as '\n'---the new line character.

If we explicitly give an (end) argument with print() function, then the print() function will print the line 
and end it with the string specified with the end argument eg.code:

print("My name is Shivansh",end="$")
print("I am 19 years old")

will print the line as :
My name is Shivansh$Iam 19 years old   
"""
print("-------------------------------------")
print("My name is Shivansh",end="$")
print("I am 19 years old")
print("-------------------------------------")
x,y=20,30
print("a=",x,end=" ")
print("b=",y)#will print in same line as end character is not a newline character but a space character.


