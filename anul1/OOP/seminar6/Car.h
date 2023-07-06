#pragma once
#include <iostream>
#include <cstring>
#include <stdlib.h>
#include "Weather.h"

class Car{

public: 
    virtual char* getName() = 0;
    virtual int getFuelCapacity() = 0;
    virtual int getFuelConsumption() = 0;
    virtual int getAverageSpeed() = 0;
    virtual int Run(Weather,int) = 0;
    virtual void setSpeed(Weather) = 0;

};