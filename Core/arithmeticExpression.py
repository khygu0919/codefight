'''
Consider an arithmetic expression of the form a#b=c.
Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.

Example

For a = 2, b = 3 and c = 5, the output should be
arithmeticExpression(a, b, c) = true.

We can replace # with a + to obtain 2 + 3 = 5, so the answer is true.

For a = 8, b = 2 and c = 4, the output should be
arithmeticExpression(a, b, c) = true.

We can replace # with a / to obtain 8 / 2 = 4, so the answer is true.

For a = 8, b = 3 and c = 2, the output should be
arithmeticExpression(a, b, c) = false.

8 + 3 = 11(not 2);
8 - 3 = 5(not 2);
8 * 3 = 24(not 2);
8 / 3 = 2.(6)(not 2).
So the answer is false.
'''
def arithmeticExpression(a, b, c):
    if a+b==c or a-b==c or a*b==c:
        return True
    elif a/float(b)==float(c):
        return True
    return False