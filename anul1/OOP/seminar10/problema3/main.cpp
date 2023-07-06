#include <iostream>
#include "vector.h"
using namespace std;

int main()
{
    MyVector v;

    v.Add(10);
    v.Add(14);
    v.Add(30);
    v.Add(650);
    v.Add(1325);

    auto filterLambda = [](int x)->bool{
        return x>100;
    };
    auto iterateLambda = [](int y)->int{
        return y+20;
    };

    cout << "Remove all elements higher than 100\n";
    v.Filter(filterLambda);
    v.Print();
    cout << "Add 20 to all elements\n";
    v.Iterate(iterateLambda);
    v.Print();

    //linux debug
    cout <<'\n';
    return 0;
}
