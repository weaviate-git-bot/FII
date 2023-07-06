#include "Mazda.h"

Mazda::Mazda()
{
    this->name = new char[10];
    strcpy(this->name, "Mazda");
    this->fuel_capacity = 30;
    this->fuel_consumption = 40;
    this->avg_speed = 110;
}
char* Mazda::getName()
{
    return this->name;
}
int Mazda::getFuelCapacity()
{
    return this->fuel_capacity;
}
int Mazda::getFuelConsumption()
{
    return this->fuel_consumption;
}
int Mazda::getAverageSpeed()
{
    return this->avg_speed;
}

void Mazda::setSpeed(Weather type)
{
    if(type==Weather::Rain)
        this->avg_speed = this->avg_speed - std::max(3,rand()%5);
    else if(type==Weather::Snow)
        this->avg_speed = this->avg_speed - std::max(10,rand()%10);
}

int Mazda::Run(Weather type, int len)
{
    this->setSpeed(type);
    int gasNeeded = (this->getFuelConsumption()*len)/100;
    if(gasNeeded>this->getFuelCapacity())
        return -1;
    int time = (len/(this->getAverageSpeed()*1.0))*60;
    return time;
}