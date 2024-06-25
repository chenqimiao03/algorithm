def gcd(a, b):
    """最大公约数
    """
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    """最小公倍数
    """
    return a // gcd(a, b) * b