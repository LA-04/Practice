import pyeda

a, b, c = map(exprvar, 'abc')
f1 = ~a & ~b & ~c | ~a & ~b & c | a & ~b & c | a & b & c | a & b & ~c
f1m, = espresso_exprs(f1.to_dnf())
print(f1m)