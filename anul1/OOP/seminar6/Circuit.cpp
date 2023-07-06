#include "Circuit.h"
using namespace std;


Circuit::Circuit()
{
    cars = new Car*[maxLen];
}
void Circuit::SetLength(int len)
{
    this->length = len;
}
void Circuit::SetWeather(Weather type)
{
    this->weather = type;
}
void Circuit::AddCar(Car* vrum)
{
    if(elements>maxLen)
    {
        realloc(cars,maxLen+maxLen/2);
        realloc(podium,maxLen+maxLen/2);
    }
    cars[elements++] = vrum;
}
void Circuit::Race()
{
    int *vec = new int[elements+10];
    for(int i=0;i<elements;i++)
        vec[i] = cars[i]->Run(weather, length);
    this->podium = vec;
}
void Circuit::ShowFinalRanks()
{
    for(int i=0;i<elements-1;i++)
        for(int j=i+1;j<elements;j++)
            if(podium[i]>podium[j])
            {
                swap(podium[i], podium[j]);
                swap(cars[i], cars[j]);
            }
            
    cout << "\n---Podium--\n";
    for(int i=0;i<elements;i++)
        if(podium[i]>=0)
            cout << cars[i]->getName() << '\n'; 
}
void Circuit::ShowWhoDidNotFinis()
{
    cout << "\n---DNF--\n";
    for(int i=0;i<elements;i++)
        if(podium[i]==-1)
            cout << cars[i]->getName() << '\n'; 
}