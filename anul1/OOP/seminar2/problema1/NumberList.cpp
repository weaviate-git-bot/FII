#include "NumberList.h"
using namespace std;

void NumberList::Init()
{
    this->count = 0;
}
bool NumberList::Add(int x)
{
    if(this->count >= 10)
        return false;
    this->numbers[this->count]=x;
    this->count++;
    return true;
    
}
void NumberList::Sort()
{
    bool sortat;
    do{
        sortat=true;
        for(int i=0;i<this->count-1;i++)
            for(int j=i+1;j<this->count;j++)
                if(this->numbers[i]>this->numbers[j])
                {
                    sortat=false;
                    swap(this->numbers[i], this->numbers[j]);
                }
    }while(!sortat);
}
void NumberList::Print()
{
    for(int i=0;i<this->count;i++)
        cout << this->numbers[i] << ' ';
    cout << '\n';
}
