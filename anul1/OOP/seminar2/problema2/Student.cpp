#include "Student.h"

std::string Student::get_name()
{
    return this->name;
}
void Student::set_name(string name)
{
    this->name = name;
}
float& Student::get_mathematics()
{
    return this->mathematics;
}
void Student::set_mathematics(float x)
{
    if(x<1 || x>10)
        return;
    this->mathematics = x;
}
float& Student::get_english()
{
    return this->english;
}
void Student::set_english(float x)
{
    if(x<1 || x>10)
        return;
    this->english = x;
}
float& Student::get_history()
{
    return this->history;
}
void Student::set_history(float x)
{
    if(x<1 || x>10)
        return;
    this->history = x;
}
float Student::Average()
{
    return (this->history+this->english+this->mathematics)/3.0;
}