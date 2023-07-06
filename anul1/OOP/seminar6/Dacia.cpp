#include "Dacia.h"

Dacia::Dacia()
{
    this->name = new char[10];
    strcpy(this->name, "Dacia");
    this->fuel_capacity = 100;
    this->fuel_consumption = 7;
    this->avg_speed = 80;
}
char* Dacia::getName()
{
    return this->name;
}
int Dacia::getFuelCapacity()
{
    return this->fuel_capacity;
}
int Dacia::getFuelConsumption()
{
    return this->fuel_consumption;
}
int Dacia::getAverageSpeed()
{
    return this->avg_speed;
}

void Dacia::setSpeed(Weather type)
{
    if(type==Weather::Rain)
        this->avg_speed = this->avg_speed - std::max(3,rand()%10);
    else if(type==Weather::Snow)
        this->avg_speed = this->avg_speed - std::max(6,rand()%20);
}

int Dacia::Run(Weather type, int len)
{
    this->setSpeed(type);
    int gasNeeded = (this->getFuelConsumption()*len)/100;
    if(gasNeeded>this->getFuelCapacity())
        return -1;
    int time = (len/(this->getAverageSpeed()*1.0))*60;
    return time;
}