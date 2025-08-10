#include <stdio.h>
int findLargest(int arr[], int n) {

    if (n <= 0) {
        printf("Error: Array is empty or has invalid size.\n");
        return -1; 
    }
    int max = arr[0];

    for (int i = 1; i < n; i++) {
       if (arr[i] > max) {
            max = arr[i];
        }
    }

    return max;
}
int main() {
    int myArray[] = {12, 75, 3, 43, 56, 13, 1};
    int size = sizeof(myArray) / sizeof(myArray[0]);

    int largestElement = findLargest(myArray, size);

    if (largestElement != -1) { 
        printf("The largest element in the array is: %d\n", largestElement);
    }

    return 0;
}
