#include <iostream>
#include "array.h"
using namespace std;

int main()
{
    Array<int> v = {100};
    Array<int> x = {100};
    //get the capacity
    try{
        x+=10;
        x+=20;
        x+=30;
        x+=40;
        x+=50;
        v=x;
        v+=25;
        v+=30;
        v+=40;
        v+=64;
        v+=978;
        v+=94;
        cout << "V has " << v.GetSize() << " elements!\n";
        cout << "Foreach print: ";
        for(auto key: v)
        {
            cout << *key << ' ';
        }
        cout << endl;
        cout << "Al 5lea element este: " << v[4] << '\n';
        cout << "Modific al 5lea element: ";
        v.Insert(4,321);
        v.Print();
        cout << "Sterg al 5lea element: ";
        v.Delete(4);
        v.Print();
        cout << "Vectorul sortat este: ";
        v.Sort();
        v.Print();
        cout << "Elementul 94 se afla pe pozitia: " << v.BinarySearch(94) <<'\n';
        cout << "Gaseste pozitia pentru care a=b+10: " << v.Find(10, [](const int& _a,const int& _b) -> int{
            if(_a==_b+10)
                return 1;
            return 0;
        });
        cout << '\n';
    }catch(Exception e)
    {
        cout <<"\n[Error] " <<  e.GetMsg() <<'\n';
    }
    //erorrs
    cout << "Erori pe operator[]";
    try{
        cout << v[-1];
    }catch(Exception e)
    {
        cout <<"\n[Error] " <<  e.GetMsg() <<'\n';
    }
    try{
        cout << v[12492];
    }catch(Exception e)
    {
        cout <<"\n[Error] " <<  e.GetMsg() <<'\n';
    }
    cout << "Empty list copy";
    try{
        Array<int> x1 = {10};
        v = x1;
    }catch(Exception e)
    {
        cout <<"\n[Error] " <<  e.GetMsg() <<'\n';
    }
    cout << "Eroare pe binary search";
    try{
        cout << v.BinarySearch(243);
    }catch(Exception e)
    {
        cout <<"\n[Error] " <<  e.GetMsg() <<'\n';
    }
    return 0;
}