from icecream import ic
ic.configureOutput(prefix='')


def parity(num: int) -> str:
    return "Even" if num % 2 == 0 else "Odd"


def prime(num: int) -> str:
    result: int = num
    if num and True == 0:
        result = 2
    d = 3
    while d * d <= num:
        if num % d == 0:
            result = d
        d = d + 2
    
    return "Prime" if result == num else "Not Prime"


def gcd(a: int, b: int) -> int:
    r = a % b
    while r != 0:
        a, b, r = b, r, (a % b)
    return b


def prime_factors(n):
    factors = {}

    def loop_divisor(num, divisor):
        while num % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            num //= divisor

        return num

    n = loop_divisor(n, 2)
    n = loop_divisor(n, 3)

    k = 5
    while n > 1 and k * k <= n:
        p1 = k
        p2 = k + 2

        n = loop_divisor(n, p1)
        n = loop_divisor(n, p2)

        k += 6

    result = ""
    if n != 1: factors[n] = 1
    for factor, count in factors.items():
        if count == 1:
            result += f"{factor} * "
        else:
            result += f"{factor}^{count} * "

    return result[:-3]


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


def direct_proof(num, expr):
    if expr == "If a number is even, then it is divisible by 2.":
        if parity(num) == "Even":
            result = f"Here, {num} is an even number since it can be written in the form of 2k where k={num // 2}. Hence, according to the definition, it is divisible by 2, validating the given statement."
        else:
            result = f"Here, {num} is not an even number, which violates our hypothesis as well as the conclusion"
    elif expr == "If a number is even, then it is not divisible by 2.":
        if parity(num) == "Even":
            result = f"Here, {num} is an even number since it can be written in the form of 2k where k={num // 2}. Hence, according to the definition, it is divisible by 2, which violates our hypothesis as well as the conclusion."
        else:
            result = f"Here, {num} is not an even number, which violates our hypothesis. However, it does apply to our conclusion, stating that our number {num} is not divisible by 2."

    return result


def ant_func(n):
    phi = int(n > 1 and n)

    for p in range(2, int(n ** 0.5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p

    if n > 1:
        phi -= phi // n

    return phi


if __name__ == "__main__":

    ic(parity(25))

    ic(prime(17))

    ic(gcd(48, 18))

    ic(prime_factors(8000))

    ic(lcm(15, 20))

    ic(direct_proof(10, "If a number is even, then it is not divisible by 2."))

    ic(ant_func(12))