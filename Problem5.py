import math


def compute():
    answer = 1
    for i in range(1, 21):
        answer *= i // math.gcd(i, answer)
    return answer


if __name__ == "__main__":
    print(compute())
    print(math.gcd(1250, 450))