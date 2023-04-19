import sys

p = sys.argv[1].split(".")
r = ''
if len(p) == 5:
    r = f"{'.'.join(p[:-1])}"
print(r)
