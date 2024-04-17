

def mdc(a,b):
    if a<b:
        return mdc(b,a)
    elif b == 0:
        return a
    else:
        return mdc(b, a % b)


print("mdc(49,42): ", mdc(,))