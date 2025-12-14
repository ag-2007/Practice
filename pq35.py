from scipy import integrate

def f(y,x):
    return x*y

res, error=integrate.dblquad(f, 0, 2, lambda x:0, lambda x:1)

print("Result", res)
print("Error", error)