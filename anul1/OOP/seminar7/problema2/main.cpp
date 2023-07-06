#include <iostream>
#include "vector.h"
#include "Masini.h"
using namespace std;

bool cmp(int a1, int a2)
{
    return a1<a2;
}

int main()
{
    Masini Ford = {50,100};
    Masini Mercedes = {50,350};
    Masini Mazda = {30,200};
    Masini Toyota = {20,50};
    Vector<Masini> v;
    v.push(Ford);
    v.push(Mercedes);
    v.push(Toyota);
    cout << "Ultima masina are capacititatea: " << v.pop().getRezervor() << '\n';
    v.insert(0,Mazda);
    v.sort();
    Masini Hyundai = {50, 180};
    v.set(3,Hyundai);
    cout << "Avem " << v.count() << " masini!\n";
    v.remove(0);
    cout << "Marca Hyundai se afla la pozitia " << v.firstIndexOf(Hyundai) << " in vector!\n";
    cout << "Marca Hyundai are capacitatea rezervorului " << v.get(Hyundai).getPutere() << "!\n";
    cout << '\n';
    return 0;
}