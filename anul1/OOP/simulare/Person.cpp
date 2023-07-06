#include "Person.h"
using namespace std;

Person::Person(string nume, int varsta,float inaltime)
{
    this->nume = nume;
    this->varsta = varsta;
    this->inaltime = inaltime;
    this->note = new int[this->maxNote];
}

void Person::addNote(int x)
{
    if(this->poz>this->maxNote)
    {
        this->maxNote*=2;
        realloc(this->note, this->maxNote);
    }
    this->note[this->poz++]=x;
}

string Person::operator[](const char* cname)
{
    string nume = cname;
    if(nume  == "nume")
        return this->nume;
    if(nume == "varsta")
        return to_string(this->varsta);
    if(nume=="inaltime")
        return to_string(this->inaltime);
    return nullptr;
}

Person::operator int()
{
    double sum =0;
    for(int i=0;i<this->poz;i++)
        sum = sum+ this->note[i];
    sum = sum/this->poz;
    if(int(sum*100)%100<50)
        return int(sum);
    return int(sum+1);
}
