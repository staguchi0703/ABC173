def resolve():
    '''
    code here
    '''
    N = int(input())
    N = N % 1000

    if N != 0:
        print(1000 - N)
    else:
        print(0)


if __name__ == "__main__":
    resolve()
