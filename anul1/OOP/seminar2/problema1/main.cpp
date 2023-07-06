#include <iostream>
#include "NumberList.h"
using namespace std;

int main()
{
    NumberList nr;
    nr.Init();
    nr.Add(20);
    nr.Add(15);
    nr.Add(30);
    nr.Print();
    nr.Sort();
    nr.Print();
    return 0;
}