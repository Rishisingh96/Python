Here's a simple example of how to implement a stack using arrays in C:
#include <stdio.h>
#define MAX 100

int stack[MAX];
int top = -1;

// Function to add an element to the stack
void push(int value) {
    if(top == MAX - 1) {
        printf("Stack Overflow\\n");
        return;
    }
    stack[++top] = value;
    printf("%d pushed to stack\\n", value);
}

// Function to remove and return the top element from the stack
int pop() {
    if(top == -1) {
        printf("Stack Underflow\\n");
        return -1;
    }
    return stack[top--];
}

// Function to view the top element of the stack
int peek() {
    if(top == -1) {
        printf("Stack is empty\\n");
        return -1;
    }
    return stack[top];
}

// Function to display the stack
void display() {
    if(top == -1) {
        printf("Stack is empty\\n");
        return;
    }
    printf("Stack: ");
    for(int i = 0; i <= top; i++)
        printf("%d ", stack[i]);
    printf("\\n");
}

int main() {
    push(10);
    push(20);
    push(30);
    display();
    printf("Popped: %d\\n", pop());
    display();
    printf("Top element: %d\\n", peek());
    return 0;
}

