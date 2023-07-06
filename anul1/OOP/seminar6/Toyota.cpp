#include "Toyota.h"

Toyota::Toyota()
{
    this->name = new char[10];
    strcpy(this->name, "Toyota");
    this->fuel_capacity = 200;
    this->fuel_consumption = 10;
    this->avg_speed = 100;
}
char* Toyota::getName()
{
    return this->name;
}
int Toyota::getFuelCapacity()
{
    return this->fuel_capacity;
}
int Toyota::getFuelConsumption()
{
    return this->fuel_consumption;
}
int Toyota::getAverageSpeed()
{
    return this->avg_speed;
}

void Toyota::setSpeed(Weather type)
{
    if(type==Weather::Rain)
        this->avg_speed = this->avg_speed - std::max(1,rand()%10);
    else if(type==Weather::Snow)
        this->avg_speed = this->avg_speed - std::max(5,rand()%15);
}

int Toyota::Run(Weather type, int len)
{
    this->setSpeed(type);
    int gasNeeded = (this->getFuelConsumption()*len)/100;
    if(gasNeeded>this->getFuelCapacity())
        return -1;
    int time = (len/(this->getAverageSpeed()*1.0))*60;
    return time;
}