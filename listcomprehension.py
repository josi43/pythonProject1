def permutation(c1,c2,c3,m):
    res=[[x,y,z]
         for x in range(c1+1)
         for y in range(c2+1)
         for z in range(c3+1)if x+y+z!=m]
    return res
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = permutation(x, y, z, n)
    print(output)