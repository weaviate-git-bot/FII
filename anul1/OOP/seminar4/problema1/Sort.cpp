#include "Sort.h"
using namespace std;

Sort::Sort(int elements, int start, int finish)
{
    this->v = new int[elements+5];
    this->size = elements;
    for(int i=0;i<this->size;i++)
    {
        this->v[i]=start+rand()%(finish-start);
    }
}

Sort::Sort(int *vec, int size)
{
    this->v = new int[size+5];
    this->size = size;
    for(int i=0;i<this->size;i++)
    {
        this->v[i] = vec[i];
    }
}
Sort::Sort(int *vec)
{
    int lastNotNull = 0;
    int i=0;
    while(i<1000)
    {
        if(vec[i]) lastNotNull=i;
        i++;
    }
    this->size = lastNotNull-1;
    this->v = new int[this->size+5];

    for(int i=0;i<this->size;i++)
        this->v[i] = vec[i];
}
Sort::Sort(int count, ...)
{
    this->size=count;
    this->v = new int[count+5];
    va_list args;
    va_start(args, count);
    for(int i=0;i<count;i++)
    {
        int x = va_arg(args,int);
        this->v[i] = x;

    }
    va_end(args);
}

Sort::Sort(char *c)
{
    char *p;
    this->v = new int[strlen(c)];
    p  = strtok(c, ",");
    int nr=0;
    while(p)
    {

        this->v[nr] = atoi(p);
        nr++;
        p = strtok(NULL, ",");
    }
    this->size = nr;
}

void Sort::InsertSort(bool ascendent) {
    for(int i=1;i<this->size;i++)
    {
        int key = this->v[i];
        int j = i-1;
        while((ascendent? key<this->v[j] : key>this->v[j]) && j>=0)
        {
            this->v[j+1]=this->v[j];
            j--;
        }
        this->v[j+1]=key;
    }
}
void Sort::QuickSort(bool ascendent)
{
    this->QuickSort(ascendent, 0, this->size-1);
}

int Sort::partition(bool ascendent,int low, int high)
{
    int pivot = this->v[high];
    int i=(low-1);
    for(int j=low;j<high;j++)
    {
        if((ascendent ? this->v[j]<pivot : this->v[j]>pivot))
        {
            i++;
            swap(this->v[i],this->v[j]);
        }
    }
    swap(this->v[i+1],this->v[high]);
    return (i+1);
}

void Sort::QuickSort(bool ascendent, int low, int high) {
    if(low<high)
    {
        int pi = this->partition(ascendent, low, high);
        this->QuickSort(ascendent, low, pi-1);
        this->QuickSort(ascendent, pi+1, high);
    }
}


void Sort::BubbleSort(bool ascendent) {
    bool sortat=true;
    do{
        sortat = true;
        for(int i=0;i<this->size-1;i++)
        {
            if((ascendent ? this->v[i]>this->v[i+1] : this->v[i]<this->v[i+1]))
            {
                sortat=false;
                swap(this->v[i], this->v[i+1]);
            }
        }
    }while(!sortat);
}
void Sort::Print() {
    for(int i=0;i<this->size;i++)
        cout << this->v[i] << ' ';
}
int Sort::GetElementsCount(){
    return this->size;
}
int Sort::GetElementFromIndex(int index){
    return this->v[index];
}