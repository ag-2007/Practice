import sympy as sp

t=sp.symbols('t')
expr=100*(sp.E)**(-0.2*t)
simp=sp.simplify(expr)
integral=sp.integrate(simp, (t, 0, 5))
print(integral)