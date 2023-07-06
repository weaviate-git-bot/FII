#include "functions.h"
#include <string>
using namespace std;

int compare_name(Student s1, Student s2)
{
    if(s1.get_name() == s2.get_name())
        return 0;
    return s1.get_name()>s2.get_name() ? 1 : -1;
}
int compare_average(Student s1, Student s2)
{
    if(s1.Average() == s2.Average())
        return 0;
    return s1.Average()>s2.Average() ? 1 : -1;
}
int compare_english(Student s1, Student s2)
{
    if(s1.get_english() == s2.get_english())
        return 0;
    return s1.get_english()>s2.get_english() ? 1 : -1;
}
int compare_math(Student s1, Student s2)
{
    if(s1.get_mathematics() == s2.get_mathematics())
        return 0;
    return s1.get_mathematics()>s2.get_mathematics() ? 1 : -1;
}
int compare_history(Student s1, Student s2)
{
    if(s1.get_history() == s2.get_history())
        return 0;
    return s1.get_history()>s2.get_history() ? 1 : -1;
}
