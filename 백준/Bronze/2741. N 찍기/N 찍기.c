#include <stdio.h>
int main()
{
    int n;
    int i = 1;
    scanf("%d", &n);
    while (1)
    {
        if (i > n)
            break;

        printf("%d\n", i);
        i++;
    }
}