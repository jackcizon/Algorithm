#include<stdio.h>
#include<math.h>
#include<config.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

typedef char* string;
#define out

string convert(int decimal, int base);

int main(int argc, char const *argv[])
{
    int decimal = 12345;
    int base_8 = 8;
    int base_16 = 16;
    string base_8_str = convert(decimal, base_8);
    string base_16_str = convert(decimal, base_16);
    printf("%s ", base_8_str);
    printf("%s ", base_16_str);
    return 0;
}

/// @brief 
/// @param decimal 
/// @param base
/// @param base_str 
string convert(int decimal, int base)
{   
    int len = 1;
    int tmp = decimal;
    while (tmp > 0)
    {
        tmp /= base;
        len ++;
    }

    string base_str = (string)calloc(sizeof(char), len);
    
    //mod
    int rem = 0;
    int index = 0;
    while (decimal > 0) 
    {
        rem = decimal % base;
        decimal /= base;
        if (rem < 10) 
        {
            base_str[index] = '0' + rem;
        } else 
        {
            base_str[index] = 'A' + rem - 10;
        }
        index++;
    }
    base_str[index] = '\0';
    //reverse
    for (size_t i = 0, j = index - 1; i < j; i++, j--)
    {
        char tmp = base_str[i];
        base_str[i] = base_str[j];
        base_str[j] = tmp;
    }      
    return base_str;    
}