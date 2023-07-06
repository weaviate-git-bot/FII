#pragma once
#include <iostream>
#include <vector>

class MyVector { 
    std::vector<int> vec;

public:

    bool Add(int); // return true if the value was added. As a result, the size of the vector increases with one.
    bool Delete(int); // returns true if the value from the index was removed. As a result, the size of the vector decreases with one.
    
    void Iterate(int(*func)(int));
    void Filter(bool(*func)(int));

    void Print();

};