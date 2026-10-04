#include <stdio.h>

int main()
{
    char huruf_h[5][6] = {
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #"};

    char huruf_a[5][6] = {
        " ### ",
        "#   #",
        "#####",
        "#   #",
        "#   #"};

    for (int i = 0; i < 5; i++)
    {
        printf("%s   %s\n", huruf_h[i], huruf_a[i]);
    }

    return 0;
}