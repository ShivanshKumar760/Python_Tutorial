#suppose we want to print something like this:
"""
Hello, world
Hello, world

1st way to thats is we write to print statements on two different line :
print("Hello, world")
print("Hello, world")

and since python print automatically prints a new line after executing first line of print statement we dont have to 
add a new line

but another way which python provide is we can use a escspe sequance in print statement which is "/n" which
provide a new line when ever we want so by using this we wont have to wait for python interpreter to rich end of line
to change the pointer to new line .


2nd way:
print("Hello world\nHello world")
"""

print("Hello world\nHello world")


#now if want to print hello world in same line we again have two ways;
print("Hello Everyone Hello Everyone")

#2nd way is to use (end),how to use end is very simple (end) help python interpreter decide whether after completion
#of print  statement we have to shift to next line or not
print("Hello ,Whats up", end = " ")
print("all good") 