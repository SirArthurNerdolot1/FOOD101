#we assume the polynomial of form ax^3+bx^2+cx+d
def slope_of_cubic(coefficients,x):
    a,b,c,d = coefficients
    slope=3*a*x**2+2*b*x+c
    return slope
values=input("Give the four coefficients with space in between: ").split(" ")
coefficients=tuple(float(x) for x in values)
x=float(input("Input value of x: "))

print(f"The slope of the polynomial at {x} for cubic is {slope_of_cubic(coefficients,x)}")