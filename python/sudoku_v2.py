'''
For this version:
find the empty positions at the first time
no need to find the empty position to fill in at each stage
'''
import time

def display(data):
    for i in range(9):
        print(data[i])
        
def solve(data,empty_spaces,head=0):
    if head>= len(empty_spaces):
        return True
    row, col = empty_spaces[head]

    lst_row = data[row]
    lst_col = [data[i][col] for i in range(9)]

    rowStart = row - row%3
    colStart = col - col%3
    lst_box = [data[rowStart+i][colStart+j] for i in range(3) for j in range(3)]
    
    for num in range(1,10):
        if data[row][col]==0 and (num not in lst_row) and (num not in lst_col) and (num not in lst_box):
            data[row][col] = num
            if solve(data,empty_spaces,head+1):
                return True            
            data[row][col] = 0
    return False


def main():
    tStart = time.time()
    data = [[8, 0, 0, 0, 0, 0, 0, 0, 0],  
            [0, 0, 3, 6, 0, 0, 0, 0, 0],  
            [0, 7, 0, 0, 9, 0, 2, 0, 0],  
            [0, 5, 0, 0, 0, 7, 0, 0, 0],  
            [0, 0, 0, 0, 4, 5, 7, 0, 0], 
            [0, 0, 0, 1, 0, 0, 0, 3, 0], 
            [0, 0, 1, 0, 0, 0, 0, 6, 8], 
            [0, 0, 8, 5, 0, 0, 0, 1, 0], 
            [0, 9, 0, 0, 0, 0, 4, 0, 0]] 

    empty_spaces = [(i,j) for i in range(9) for j in range(9) if data[i][j] == 0]     
    if solve(data,empty_spaces):
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