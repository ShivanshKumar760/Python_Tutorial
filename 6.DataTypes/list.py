'''
List
Python Lists are similar to arrays in C. However, the list can contain data of different types. The items stored in the list are separated with a comma (,) and enclosed within square brackets [].

We can use slice [:] operators to access the data of the list. The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.

Consider the following example.

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  
'''

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  