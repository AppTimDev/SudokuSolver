/*
Soultion:
[8, 1, 2, 7, 5, 3, 6, 4, 9]
[9, 4, 3, 6, 8, 2, 1, 7, 5]
[6, 7, 5, 4, 9, 1, 2, 8, 3]
[1, 5, 4, 2, 3, 7, 8, 9, 6]
[3, 6, 9, 8, 4, 5, 7, 2, 1]
[2, 8, 7, 1, 6, 9, 5, 3, 4]
[5, 2, 1, 9, 7, 4, 3, 6, 8]
[4, 3, 8, 5, 2, 6, 9, 1, 7]
[7, 9, 6, 3, 1, 8, 4, 5, 2]
*/
function display(data) {
    for (const row of data) {
        let str = ''
        for (const num of row) {
            str += num + ' '
        }
        console.log(str);
    }
}

function isInsideRow(data, row, num) {
    return data[row].indexOf(num) > -1
}

function isInsideColumn(data, col, num) {
    for (let i = 0; i < 9; i++) {
        if (data[i][col] == num) {
            return true
        }
    }
    return false
}

function isInsideBox(data, row, col, num) {
    const rowStart = row - row % 3
    const colStart = col - col % 3
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (data[rowStart + i][colStart + j] == num) {
                return true
            }
        }
    }
    return false
}

function canFill(data, row, col, num) {
    return data[row][col] == 0 && !isInsideRow(data, row, num) && !isInsideColumn(data, col, num) && !isInsideBox(data, row, col, num)
}

function findEmptyPos(data) {
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (data[i][j] == 0) {
                return {
                    row: i,
                    col: j
                }
            }
        }
    }
    return null
}

function solve(data) {
    const pos = findEmptyPos(data)
    if (pos === null) {
        //no empty position
        return true
    }
    const {
        row,
        col
    } = pos

    for (let num = 1; num <= 9; num++) {
        if(canFill(data, row, col, num)){
            data[row][col] = num
            if(solve(data)) return true
            data[row][col] = 0
        }
    }
    return false
}

const data = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

if (solve(data)) {
    display(data);
}else{
    console.log('No solution!!');    
}