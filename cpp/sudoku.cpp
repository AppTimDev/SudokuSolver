#include <iostream>
using namespace std;
#include <chrono>
using namespace std::chrono;

void display(int data[9][9]){
    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            cout << data[i][j] << " " ;                
        }
        cout << endl;           
    }
}

bool isInsideRow(int data[9][9],int row, int num){
    for (int i = 0; i < 9; i++){
        if(data[row][i]==num){
            return true;
        }
    }
    return false;
}
bool isInsideColumn(int data[9][9],int col, int num){
    for (int i = 0; i < 9; i++){
        if(data[i][col]==num){
            return true;
        }
    }
    return false;
}
bool isInsideBox(int data[9][9],int row, int col, int num){
    int rowStart = row - row%3;
    int colStart = col - col%3;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if(data[rowStart+i][colStart+j]==num){
                return true;
            }
        }
    }
    return false;
}
bool canFill(int data[9][9],int row, int col, int num){
    return data[row][col]==0&& !isInsideRow(data,row,num)&& !isInsideColumn(data,col,num)&& !isInsideBox(data,row,col,num);
}

// bool findEmptyPos(int data[9][9], int &row, int &col){
//     for (int i = 0; i < 9; i++){
//         for (int j = 0; j < 9; j++){
//             if(data[i][j]==0){
//                 row = i;
//                 col = j;
//                 return true;
//             }
//         }
//     }
//     return false;
// }
void findEmptyPos(int data[9][9], int pos[2]){
    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++){
            if(data[i][j]==0){
                pos[0] = i;
                pos[1] = j;
                return;
            }
        }
    }
}



bool solve(int data[9][9]){
    // int row,col;

    // if(!findEmptyPos(data, row,col)){
    //     return true;
    // }
    int pos[2] = {-1,-1};
    findEmptyPos(data, pos);
    int row = pos[0], col= pos[1];
    if(row==-1 && col==-1){
        //finish
        return true;
    }

    for (int num = 1; num <= 9; num++) {
        if(canFill(data,row,col,num)){            
            data[row][col] = num;
            if(solve(data)){
                return true;
            }
            data[row][col] = 0;
        }
    }
    return false;
}

int main()  
{
    int data[9][9] = {{8, 0, 0, 0, 0, 0, 0, 0, 0},  
                      {0, 0, 3, 6, 0, 0, 0, 0, 0},  
                      {0, 7, 0, 0, 9, 0, 2, 0, 0},  
                      {0, 5, 0, 0, 0, 7, 0, 0, 0},  
                      {0, 0, 0, 0, 4, 5, 7, 0, 0}, 
                      {0, 0, 0, 1, 0, 0, 0, 3, 0}, 
                      {0, 0, 1, 0, 0, 0, 0, 6, 8}, 
                      {0, 0, 8, 5, 0, 0, 0, 1, 0}, 
                      {0, 9, 0, 0, 0, 0, 4, 0, 0}};  

    cout << "---------------------" <<endl;
    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    if (solve(data)){
        //print answer
        display(data);
        /***
            8 1 2 7 5 3 6 4 9
            9 4 3 6 8 2 1 7 5
            6 7 5 4 9 1 2 8 3
            1 5 4 2 3 7 8 9 6
            3 6 9 8 4 5 7 2 1
            2 8 7 1 6 9 5 3 4
            5 2 1 9 7 4 3 6 8
            4 3 8 5 2 6 9 1 7
            7 9 6 3 1 8 4 5 2
        ***/
    }        
    else{
        cout << "No solution!!" <<endl;
    }  
    high_resolution_clock::time_point t2 = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>( t2 - t1 ).count();
    cout << "Time taken by function: "<< duration << " microseconds" << endl;    

    return 0;  
}  