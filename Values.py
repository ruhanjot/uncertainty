import math

class Values:
    def __init__(self, actual, absolute_unc):
        self.actual = actual
        self.absolute_unc = absolute_unc
   
    def __repr__(self):
        return str("Values(" + str(self.actual) + "," + str(self.absolute_unc) + ")")
   
    def __str__(self):
        return (str(self.actual) + " ± " + str(self.absolute_unc))

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)

    def __mul__(self, other):
        return multiply(self, other)

    def __truediv__(self, other):
        return divide(self, other)
    
    def __pow__(self, other):
        return power(self, other)
    
    def __radd__(self, other):
        return add(other, self)

    def __rsub__(self, other):
        return subtract(other, self)

    def __rmul__(self, other):
        return multiply(other, self)

    def __rtruediv__(self, other):
        return divide(other, self)
    
    def __rpow__(self, other):
        return power(other, self)

    def output_range(self):
        upper = self.actual + self.absolute_unc
        lower = self.actual - self.absolute_unc
        return ("[" + str(lower) + ", " + str(upper) + "]")


#Functions.py
def add(val1, val2):
    val1_isValue = isinstance(val1, Values)
    val2_isValue = isinstance(val2, Values)

    if val1_isValue and val2_isValue:
        actual = val1.actual + val2.actual
        absolute = val1.absolute_unc + val2.absolute_unc
        return Values(actual, absolute)
    elif val1_isValue and not val2_isValue:
        return Values_and_number(val1, val2, "+")
    elif not val1_isValue and val2_isValue:
        return Values_and_number(val2, val1, "+", True) 


def subtract(val1, val2):
    val1_isValue = isinstance(val1, Values)
    val2_isValue = isinstance(val2, Values)

    if val1_isValue and val2_isValue:
        actual = val1.actual - val2.actual
        absolute = val1.absolute_unc + val2.absolute_unc
        return Values(actual, absolute)
    elif val1_isValue and not val2_isValue:
        return Values_and_number(val1, val2, "-")
    elif not val1_isValue and val2_isValue:
        return Values_and_number(val2, val1, "-", True) 


def multiply(val1, val2):
    val1_isValue = isinstance(val1, Values)
    val2_isValue = isinstance(val2, Values)

    if val1_isValue and val2_isValue:
        actual = val1.actual * val2.actual
        absolute = abs(val1.absolute_unc * val2.actual) + \
            abs(val2.absolute_unc * val1.actual)
        return Values(actual, absolute)
    elif val1_isValue and not val2_isValue:
        return Values_and_number(val1, val2, "*")
    elif not val1_isValue and val2_isValue:
        return Values_and_number(val2, val1, "*", True)


def divide(val1, val2):
    val1_isValue = isinstance(val1, Values)
    val2_isValue = isinstance(val2, Values)

    if val1_isValue and val2_isValue:
        if val2.actual != 0:
            actual = val1.actual / val2.actual
            absolute = abs(val1.absolute_unc / val2.actual) + \
                abs(val2.absolute_unc * val1.actual / pow(val2.actual, 2))
            return Values(actual, absolute)
        else:
            print("Trying to divide by zero! " + "Values 1: " +
                str(val1) + "Values 2: " + str(val2))
            return "Failure to divide by zero. Please see console."
    elif val1_isValue and not val2_isValue:
        return Values_and_number(val1, val2, "/")
    elif not val1_isValue and val2_isValue:
        return Values_and_number(val2, val1, "/", True)    
        

def power(val1, n):
    if isinstance(val1, Values) and not isinstance(n, Values):
        if val1.actual != 0 and n != 0:
            actual = pow(val1.actual, n)
            uncertainty = n * val1.absolute_unc
            return Values(actual, uncertainty)
        else:
            print("Trying to do 0 to the power of 0")
            print("Value is " + str(val1), " and the number is " + str(n))
            return("Check console please.")
    else:
        print("The value is " + str(val1) + " and the number is " + str(n))
        print("So the power function cannot work on these because it is only available for integer exponents")


def scale(val1, amount):
    actual = amount * val1.actual
    absolute_unc = amount * val1.absolute_unc
    return Values(actual, absolute_unc)


def average(val1, val2):
    return scale(add(val1, val2), 0.5)


def Values_and_number(values, number, oper, reverse = False):
    if oper == "+":
        actual = values.actual + number
        ans = Values(actual, values.absolute_unc)
        return ans
    elif oper == "-":
        if reverse:
            actual = number - values.actual
            ans = Values(actual, values.absolute_unc)
            return ans
        else:
            actual = values.actual - number
            ans = Values(actual, values.absolute_unc)
            return ans
    elif oper == "*":
        ans = scale(values, number)
        return ans
    elif oper == "/":
        if number != 0:
            if reverse:
                actual = number / values.actual
                absolute = values.absolute_unc * number / pow(values.actual, 2)
                ans = Values(actual, absolute)
                return ans
            else:
                ans = scale(values, 1 / number)
                return ans
        else:
                print("Trying to divide Values by zero! " + "Values 1: " +
                    str(values) + "number : " + str(number))
                return "Failure to divide by zero. Please see console."
    elif oper == "^":
        ans = power(values, number)
        return ans
    else:
        print("Error at values_and_number function.")
        print("Oper is " + oper + " and values is " + str(values) + ". Number is " + str(number))
