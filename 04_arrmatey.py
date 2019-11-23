import sys

x = sys.argv
print(x)

i = 0

for ch in x:
    print("Argv of ", i, "is ", ch)
    i = i+1

new_order = sorted(x, key = lambda y: -len(y))

for h in new_order:
    print(h)






