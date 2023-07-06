#include <iostream>
#include <algorithm>
#include "Car.h"


class Circuit{
private: 
    int length;
    Weather weather;
    Car** cars;
    int maxLen = 100;
    int elements = 0;
    int *podium;
public:
    Circuit();
    void SetLength(int);
    void SetWeather(Weather);
    void AddCar(Car*);
    void Race();
    void ShowFinalRanks();
    void ShowWhoDidNotFinis();

};