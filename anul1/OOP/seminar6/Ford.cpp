#include "Ford.h"

Ford::Ford()
{
    this->name = new char[10];
    strcpy(this->name, "Ford");
    this->fuel_capacity = 50;
    this->fuel_consumption = 10;
    this->avg_speed = 110;
}
char* Ford::getName()
{
    return this->name;
}
int Ford::getFuelCapacity()
{
    return this->fuel_capacity;
}
int Ford::getFuelConsumption()
{
    return this->fuel_consumption;
}
int Ford::getAverageSpeed()
{
    return this->avg_speed;
}

void Ford::setSpeed(Weather type)
{
    if(type==Weather::Rain)
        this->avg_speed = this->avg_speed - std::max(5,rand()%15);
    else if(type==Weather::Snow)
        this->avg_speed = this->avg_speed - std::max(10,rand()%25);
}

int Ford::Run(Weather type, int len)
{
    this->setSpeed(type);
    int gasNeeded = (this->getFuelConsumption()*len)/100;
    if(gasNeeded>this->getFuelCapacity())
        return -1;
    int time = (len/(this->getAverageSpeed()*1.0))*60;
    return time;
}