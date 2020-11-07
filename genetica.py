def solution():
    c = int(input())
    text = input()
    answer = False

    for i in range(0, len(text) - c):
        if(len(text[i:i + c]) == c and is_palindrome(text[i:i + c])):
            answer = True
    if(answer):
        print('S')
    else:
        print('N')


def is_palindrome(string):
    low = 0
    high = len(string) - 1

    for i in range(0, int(high / 2)):
        if string[i] != string[high - i]:
            return False
    return True


solution()
