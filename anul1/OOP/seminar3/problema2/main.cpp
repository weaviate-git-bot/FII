#include <iostream>
#include "Canvas.h"
using namespace std;

int main()
{
    Canvas c = Canvas(20,20);
    
    // c.DrawLine();
    c.SetPoint(9,19, 'x');
    c.DrawLine(10,10,16,16,'y');
    c.FillRect(1,1,4,5,'r');
    c.DrawRect(1,7,4,10,'l');
    c.Print();
    c.Clear();
    cout << "-----------------------------\n";
    c.FillCircle(10,10,8,'a');
    c.Print();
    c.Clear();
    cout << "-----------------------------\n";
    c.DrawCircle(10,10,8,'c');
    c.Print();

    c.Clear();
    cout << '\n';
    return 0;
}