def gcd(a, b):
    if a % b == 0:
        return b
    else:
        a, b = b, a % b
        return gcd(a, b)


def lcm(a, b):
    return (a * b // gcd(a, b))


a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
