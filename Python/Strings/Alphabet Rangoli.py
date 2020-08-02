def print_rangoli(size):
    for i in range(n):
        size = "-".join(chr(ord('a') + n - j - 1) for j in range(i + 1))
        print((size + size[::-1][1:]).center(n * 4 - 3, '-'))

    for i in range(n - 1):
        size = "-".join(chr(ord('a') + n - j - 1) for j in range(n - i - 1))
        print((size + size[::-1][1:]).center(n * 4 - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
