def resolve():
    '''
    code here
    '''
    import itertools

    H, W, K = [int(item) for item in input().split()]
    grid = [[item for item in input().split()] for _ in range(H)]


    def counter(temp_grid):
        print(temp_grid)
        cnt = 0
        for i in range(H):
            for j in range(W):
                if temp_grid[i][j] == '#':
                    cnt += 1
        if cnt == K:
            return 1
        else:
            return 0

    res = 0
    temp_list = []
    for line in grid:
        temp_list += line
    
    for 


    # print(cnt)


if __name__ == "__main__":
    resolve()
