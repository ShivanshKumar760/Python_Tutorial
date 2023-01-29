"""

in this provide before moving on to 3rd way to greet lets see the syntax of fstring:-

print(f"STATEMENT{variable}") its important to provide a curly bracket to hold variable so that
when python interprets the line it knows that variable is encountered in print() function under
double qoute and then it will fetch the variable value and then format the string 


but just having curly bracket is not gonna work before double quotes its necessary to provide

f"" in order for format string to work."""

variable="world"

print(f"hello,{variable}")#correct syntax

print(f"hello,variable")#will not genrate the correct output since we have not given curly bracket{} it will take "hello,variable" as one entity

print("hello{variable}")#this will give output hello{variable} cause we have not given f before  double qoute.