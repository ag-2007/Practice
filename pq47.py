import sympy as sp

t=sp.symbols('t')
expr=5*t**2+10*t-(3*t**2-4*t+6)
expanded=sp.expand(expr)
factored=sp.factor(expanded)
value=factored.subs(t,2)
print(value)


