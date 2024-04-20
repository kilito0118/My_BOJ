#include <stdio.h>
#include <stdlib.h>

int queue[10000000];
int front = 0;
int rear = 0;
void enqueue(int data)
{
    if ((rear + 1) % 10000000 == front)
    {
        // printf("Queue is full\n");
        return;
    }
    rear = (rear + 1) % 10000000;
    queue[rear] = data;
}

int dequeue()
{
    if (front == rear)
    {
        // printf("Queue is empty\n");
        return;
    }
    front = (front + 1) % 10000000;
    return queue[front];
}

void find_seq(int a, int b)
{

    for (int i = 1; i <= a; i++)
        enqueue(i);
    for (int j = 0; j < a; j++)
    {
        if (front == rear)
        {
            break;
        }
        for (int i = 0; i < b - 1; i++)
        {
            enqueue(dequeue());
        }
        printf("%d", dequeue());
        if (j == a - 1)
            break;
        printf(", ");
    }
}

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("<");
    find_seq(a, b);
    printf(">");
    return 0;
}