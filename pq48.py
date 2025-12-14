import sympy as sp

t=sp.symbols('t')
expr=3*t**3-5*t**2+4*t
vel=sp.diff(expr)
accel=sp.diff(vel)
v_3=vel.subs(t, 3)
print(v_3)

