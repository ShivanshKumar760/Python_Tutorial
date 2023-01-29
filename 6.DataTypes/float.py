'''
A Number having fractional part is a floating point number.For example,3.14159 is a floating point number 
The decimal point signals that it is a floating point number,not an integer.The number 12 is an
integer ,but 12.0 is a floating point number.

fractional number can be written in two forms :

i)Fractional form(Normal Decimal Notation)eg:3500.75,0.00005,147.9101 etc.

ii)Exponent Notation eg: 3.50075E03 ,0.5E-04, 1.479101E02 etc.

Floating point variable represent real numbers , which are used for measurable quantities like 
distance ,area,temperature,etc. and typically have a fractional part.

Floating point number have two advantage over integer :
    a)they can represent values between the integer 
    b)they can represent a much greater range of values .
    
But Floating point numbers suffer from one disadvantage also:
    a)Floating point operations are usually slower than integer operations

in Python ,floating point number represent machine level double precision floating point numbers
(15 digit precision).The range of these numbers is limited by the underlying machine architecture
subject to available virtual memory.
'''

#To declare a float  type variable choose a variable name and then provide a value with a decimal
# pointe number
b = 40.5  
print("The type of b", type(b))#this should print float data type class