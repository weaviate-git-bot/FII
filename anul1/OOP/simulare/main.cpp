#include <iostream>
#include <string>
#include "Person.h"
using namespace std;

int main()
{
    Person p = { "Ionut", 26, 1.83 };
    cout << p["nume"] << " are " << p["varsta"] << " ani" << endl;


    p.addNote(3);
    p.addNote(7);
    p.addNote(8);
    p.addNote(10);

    cout << int(p) << endl; // Afiseaza media aritmetica a notelor;
    
    return 0;
}