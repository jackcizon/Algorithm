#include<stdio.h>
#include<config.h>
#include<stdlib.h>
#include<string.h>

#define out

void linearConv(int* x, int* h, out int* y, int M, int N);
void cyclicConv(int* x, int* h, out int* y, int M, int N);

int main(int argc, char const *argv[])
{
    int x[] = {1, 2, 3, 4};
    int h[] = {1, 1, 1, 1};
    int len_x = sizeof(x) / sizeof(x[0]);
    int len_h = sizeof(h) / sizeof(h[0]);
    //int y[len_x + len_h - 1];
    int len_y = len_h + len_x - 1;
    int* y = (int*)malloc(len_y * sizeof(int));
    linearConv(x, h, y, len_x, len_h);

    int len_cy = len_x + len_h - 1;
    int* cy = (int*)malloc(len_cy * sizeof(int));
    cyclicConv(x, h, cy, len_x, len_h);

    for (size_t i = 0; i < len_y; i++)
    {
        printf("%d ", y[i]);
    }
    free(y);
    puts("");

    for (size_t i = 0; i < len_cy; i++)
    {
        printf("%d ", cy[i]);
    }
    free(cy);

    return 0;
}


void linearConv(int* x, int* h, out int* y, int M, int N)
{
    for (size_t i = 0; i < M + N - 1; i++)
    {
        y[i] = 0;
        for (size_t j = 0; j < N; j++)
        {
            if (i >= j and i < M + j)   // i belogs to [j, M + j)
            {
                y[i] += h[j] * x[i - j];    // i - j belongs to [0, M)
            }       
        }
    }
}

void cyclicConv(int* x, int* h, out int* cy, int M, int N)
{
    for (size_t i = 0; i < M; i++)
    {
        cy[i] = 0;
        for (size_t j = 0; j < N; j++)
        {
            size_t index = (i - j + M) % M;
            cy[i] += h[j] * x[index];
        }
    }
}