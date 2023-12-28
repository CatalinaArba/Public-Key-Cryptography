


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)



def lcm(a, b):
    return (a*b) // gcd(a, b)


def pollardsPMinus1(n, B):
    k=1
    for i in range(1, B+1):
        k = lcm(k, i)


    a=2
    d = gcd(pow(a, k, n)-1, n)

    if 1< d <n:
        return d
    else:
        return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        number = int(input("Enter the number: "))
        inputB = int(input("Enter the bound (B): "))

        factor = pollardsPMinus1(number, inputB)
        if factor:
            print("A factor is ", factor)
            other_factor = number // factor
            print("The other factor is ", other_factor)
            print(f"{number} = {factor} * {other_factor}")
        else:
            print("The given number is a prime number")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
