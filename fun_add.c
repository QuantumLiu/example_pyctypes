#include <stdlib.h>

//matAdd1 reference https://www.pythonheidong.com/blog/article/761228/958dfbbc06fa03410228/
void matAdd1(const int ROW, const int COL, const int x[][COL], const int y[][COL], int z[][COL]){
    int i, j;
    for (i = 0; i < ROW; i++){
        for (j = 0; j < COL; j++){
            z[i][j] = x[i][j] + y[i][j];
        }
    }
}

void matAdd2(const int ROW, const int COL, const int* x, const int* y, int* z){
    int i, j;
    for (i = 0; i < ROW; i++){
        for (j = 0; j < COL; j++){
            z[i*COL+j] = x[i*COL+j] + y[i*COL+j];
        }
    }
}