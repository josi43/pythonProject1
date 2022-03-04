def swap_case(s):
    n=0
    lista=[]
    final = ''
    for i in s:
        if s[n].isupper():
            mai = s[n].lower()
            lista.append(mai)
        else:
            men= s[n].upper()
            lista.append(men)
        n+=1

    for i in lista:
        final += i
    return final

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
