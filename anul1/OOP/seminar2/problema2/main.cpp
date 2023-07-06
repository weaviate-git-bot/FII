#include <iostream>
#include "Student.h"
#include "functions.h"
using namespace std;

int main()
{
    Student s1, s2;
    s1.set_name("Bogdan");
    s2.set_name("Ioana");

    s1.set_english(7);
    s1.set_mathematics(10);
    s1.set_history(5);

    s2.set_english(9);
    s2.set_mathematics(5);
    s2.set_history(10);

    cout << s1.get_name() << "'s average is " << s1.Average() << endl;
    cout << s2.get_name() << "'s average is " << s2.Average() << endl;

    cout << "Comparison:\n";
    cout << "1 means that " << s1.get_name() << " is bigger, \n0 means both are equal and -1 means that\n";
    cout << s2.get_name() << " is bigger.\n---------------------------\n";
    
    cout << "Name: " << compare_name(s1, s2) << endl;
    cout << "Average: " << compare_average(s1, s2) << endl;
    cout << "English grade: " << compare_english(s1, s2) << endl;
    cout << "Mathematics grade: " << compare_math(s1, s2) << endl;
    cout << "History grade: " << compare_history(s1, s2) << endl;

    cout << '\n';
    return 0;
}