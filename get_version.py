import sys

v = sys.argv[1]
p = v.split(".")
r = ''
if len(p) == 4:
    n = int(p[-1]) + 1
    r = f"{'.'.join(p[:-1])}.{n}"
else:
    if len(p) > 4:
        n = 1
        r = f"{'.'.join(p)}.{n}"


print(r)
