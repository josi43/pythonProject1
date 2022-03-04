
# Complete the solve function below.
def solve(s):
    if s[0].islower():
        s= s.upper()
        return s
    else:
        s[0].upper()
        return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
