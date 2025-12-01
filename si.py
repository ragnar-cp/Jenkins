import sys

if len(sys.argv) != 4:
    print("Usage: python3 si.py <principal> <rate> <time>")
    sys.exit(1)

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

si = (principal * rate * time) / 100
print("Simple Interest:", si)
