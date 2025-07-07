#include <stdio.h>  // Required for printf and scanf

// function declaration
int add(int x, int y);

int main() {
    int x, y;

    // Input for x
    printf("x is equal to: ");
    scanf("%d", &x);

    // Input for y
    printf("y is equal to: ");
    scanf("%d", &y);

    // call function
    int result = add(x, y);
    printf("Result: %d\n", result);
    return 0;
}

// function definition
int add(int x, int y) {
    return x + y;
}

