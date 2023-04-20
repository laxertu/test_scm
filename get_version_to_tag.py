import sys

p = sys.argv[1].split(".")
r = f"{p[0]}.{p[1]}.{p[2]}.{int(p[3]) + 1}"
print(r)
