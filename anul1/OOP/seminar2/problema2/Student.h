#pragma once
#include <string>
using namespace std; 

class Student
{
    string name;
    float mathematics;
    float english;
    float history;
    public:
        string get_name();
        void set_name(string name);
        float& get_mathematics();
        void set_mathematics(float x);
        float& get_english();
        void set_english(float x);
        float& get_history();
        void set_history(float x);
        float Average();
};