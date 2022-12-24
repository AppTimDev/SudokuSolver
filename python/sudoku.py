import time

def display(data):
    for i in range(9):
        print(data[i])

def isInsideRow(data,row, num):
    return num in data[row]
    # for i in range(9):
    #     if data[row][i]==num:
    #         return True
    # return False

def isInsideColumn(data,col, num):
    lst_col = [data[i][col] for i in range(9)]
    return num in lst_col

    # for i in range(9):
    #     if data[i][col]==num:
    #         return True
    # return False

def isInsideBox(data, row, col, num):
    rowStart = row - row%3
    colStart = col - col%3
    for i in range(3):
        for j in range(3):
            if data[rowStart+i][colStart+j]==num:
                return True
    return False

def canFill(data,row, col, num):
    return data[row][col]==0 and not isInsideRow(data,row,num) and not isInsideColumn(data,col,num) and not isInsideBox(data,row,col,num)

def findEmptyPos(data, pos):
    for i in range(9):
        for j in range(9):
            if data[i][j]==0:
                pos[0] = i
                pos[1] = j
                return None


def solve(data):
    pos = [-1,-1]
    findEmptyPos(data, pos)
    row, col = pos
    if row==-1 and col==-1:
        return True   

    
    for num in range(1,10):
        if canFill(data,row,col,num):
            data[row][col] = num
            if solve(data):
                return True            
            data[row][col] = 0
    return False


def main():
    data = [[8, 0, 0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 3, 6, 0, 0, 0, 0, 0],  
            [0, 7, 0, 0, 9, 0, 2, 0, 0],  
            [0, 5, 0, 0, 0, 7, 0, 0, 0],  
            [0, 0, 0, 0, 4, 5, 7, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 3, 0], 
            [0, 0, 1, 0, 0, 0, 0, 6, 8], 
            [0, 0, 8, 5, 0, 0, 0, 1, 0], 
            [0, 9, 0, 0, 0, 0, 4, 0, 0]] 


    tStart = time.time()

    if solve(data):
        display(data)
        '''
            8 1 2 7 5 3 6 4 9
            9 4 3 6 8 2 1 7 5
            6 7 5 4 9 1 2 8 3
            1 5 4 2 3 7 8 9 6
            3 6 9 8 4 5 7 2 1
            2 8 7 1 6 9 5 3 4
            5 2 1 9 7 4 3 6 8
            4 3 8 5 2 6 9 1 7
            7 9 6 3 1 8 4 5 2
        '''            
    else:
        print("No solution!!")

    print ("time used: %.3fs" % (time.time() - tStart))

  
if __name__ == "__main__":
    main()