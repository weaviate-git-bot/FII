#include <iostream>
#include "Sort.h"
using namespace std;

int main()
{
    //1. create the list that needs to be sorted out of random values within a specific interval (min , max). The constructor will receive 3 parameters (the number of elements in the list, minimum value, maximum value).
    Sort first(7,2,5);
    first.BubbleSort();
    first.Print();
    cout << "\n----------------------------\n";
    int *arr = new int[5]{1234,534,534,654,6};
    Sort second(arr);
    second.InsertSort(true);
    second.Print();
    cout << "\n----------------------------\n";
    int n=6;
    int *arr2 = new int[n]{1239,423,56,36,7,5};
    Sort third(arr2,n);
    third.QuickSort();
    third.Print();
    cout << "\n----------------------------\n";
    Sort forth ={5,10,60,40,30,50};
    forth.BubbleSort(true);
    forth.Print();
    cout << "\n----------------------------\n";
    char numbers[]="10,5643,432,234,654,12";
    Sort fifth(numbers);
    fifth.InsertSort();
    fifth.Print();
    cout << "\n----------------------------\n";

    cout << '\n';
    return 0;
}