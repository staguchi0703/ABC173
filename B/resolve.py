def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    S = [input() for _ in range(N)]
    dict1 = collections.Counter(S)

    print('AC x', dict1['AC'])
    print('WA x', dict1['WA'])
    print('TLE x', dict1['TLE'])
    print('RE x', dict1['RE'])

if __name__ == "__main__":
    resolve()
