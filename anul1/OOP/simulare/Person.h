#include <string>

class Person
{
    std::string nume;
    int varsta;
    float inaltime;
    int *note;
    int maxNote = 100;
    int poz=0;

public:
    Person(std::string,int,float);
    void addNote(int x);
    operator int();
    std::string operator[](const char*);
    
};