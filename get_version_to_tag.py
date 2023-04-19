import sys

v = sys.argv[1]
p = v.split(".")
r = ''
if len(p) == 5:
    n = int(p[-1]) + 1
    r = f"{'.'.join(p[:-2])}.{n}"
print(r)
