#include <iostream>
#include "Math.h"
using namespace std;

int main()
{
    cout << "Adun 2 inturi: " << Math::Add(10,20) << '\n';
    cout << "Adun 3 inturi: " << Math::Add(10,20,30) << '\n';
    cout << "Adun 2 double: " << Math::Add(1.20, 2.20) << '\n';
    cout << "Adun 3 double : " << Math::Add(5.4,3.6,8.1) << '\n';
    cout << "Adun un int si un double : " << Math::Add(1,2.3) << '\n';
    cout << "Inmultesc 2 inturi: " << Math::Mul(10,20) << '\n';
    cout << "Inmultesc 3 inturi: " << Math::Mul(10,20,30) << '\n';
    cout << "Inmultesc 2 double: " << Math::Mul(1.2,2.0) << '\n';
    cout << "Inmultesc 3 doubel: " << Math::Mul(1.2,2.0,5.3) << '\n';
    cout << "Inmultesc x inturi: " << Math::Add(6,1,2,3,4,5,30) << '\n';
    cout << "Adun doua siruri: " << Math::Add("10","24235230") << '\n';

    //linux debug
    cout << '\n';
    return 0;
}