#include "Mercedes.h"

Mercedes::Mercedes()
{
    this->name = new char[10];
    strcpy(this->name, "Mercedes");
    this->fuel_capacity = 400;
    this->fuel_consumption = 30;
    this->avg_speed = 150;
}
char* Mercedes::getName()
{
    return this->name;
}
int Mercedes::getFuelCapacity()
{
    return this->fuel_capacity;
}
int Mercedes::getFuelConsumption()
{
    return this->fuel_consumption;
}
int Mercedes::getAverageSpeed()
{
    return this->avg_speed;
}

void Mercedes::setSpeed(Weather type)
{
    if(type==Weather::Rain)
        this->avg_speed = this->avg_speed - std::max(1,rand()%5);
    else if(type==Weather::Snow)
        this->avg_speed = this->avg_speed - std::max(3,rand()%10);
}

int Mercedes::Run(Weather type, int len)
{
    this->setSpeed(type);
    int gasNeeded = (this->getFuelConsumption()*len)/100;
    if(gasNeeded>this->getFuelCapacity())
        return -1;
    int time = (len/(this->getAverageSpeed()*1.0))*60;
    return time;
}