"""
Broadly lvalue and rvalue can be thought of as:

Lvalue :-expression that can come on the LHS(left hand side) of an assignment.

Rvalue :-expression that can come on the RHS(right hand side) of an assignment.

Basically Lvalue are the objects to which we can assign values or expression.Lvalue can come on lhs of rhs of
an assignment.

Rvalue are the literals and expressions that are assigned to lvalues.Rvalue can come on rhs of an assignment statement

"""

#Example:

a=20 # a is lvaue and 20 is rvalue
print(a)

#print("This part of the code will generate error")

#but we cannot say:
"""
20=a #this will genrate error numeric are the values assigned to lhs

#or 
a*2=b #expression is should come on rhs of an assignment statement


"""