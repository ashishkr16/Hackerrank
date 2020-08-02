def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        chars = ""
        for j in range(i, i+k):
            if string[j] not in chars:
                chars += string[j]
                print(string[j], end='')
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)