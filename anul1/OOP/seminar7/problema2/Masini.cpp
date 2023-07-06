#include "Masini.h"

Masini::Masini()
{
    rezervor=0;
    putere=0;
}
Masini::Masini(int rezervor,int putere)
{
    this->rezervor = rezervor;
    this->putere = putere;
}
int Masini::getPutere() const
{
    return this->putere;
}
int Masini::getRezervor() const
{
    return this->rezervor;
}
bool operator<(const Masini& a, const Masini& b)
{
    return (a.putere < b.getPutere());
}
bool operator==(const Masini& a, const Masini& b)
{
    return (a.rezervor == b.getRezervor());
}