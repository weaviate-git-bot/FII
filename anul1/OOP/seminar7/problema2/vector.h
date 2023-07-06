#include <iostream>
using namespace std;
template <typename T>
class Vector
{
    T *arr;
    int size=100;
    T err_obj;
public: 
    int poz=0;

    Vector()
    {
        arr = new T[this->size];
    }

    
    void push(const T &a)
    {
        if(this->poz>=this->size)
        {
            this->size*=2;
            realloc(arr, this->size);
        }
        this->arr[this->poz++]=a;
    }
    
    T& pop()
    {
        return this->arr[this->poz-1];
    }
    
    void remove(const int s)
    {
        if(s>=this->poz)
            return;
        for(int i=s;i<this->poz;i++)
            this->arr[i] = this->arr[i+1];
        this->poz--;
    }

    void insert(int loc, const T &a)
    {
        if(loc>this->poz)
        {
            this->arr[this->poz++]=a;
            return;
        }
        for(int i=this->poz;i>loc;i--)
            this->arr[i]=this->arr[i-1];
        this->arr[loc]=a;
        this->poz++;

    }
    void sort(bool(*func)(T x,T y)=nullptr)
    {
        for(int i=0;i<this->poz-1;i++)
            for(int j=i+1;j<this->poz;j++)
            {
                if((func==nullptr? this->arr[i]<this->arr[j] : func(arr[i], arr[j])))
                {
                    swap(this->arr[i], this->arr[j]);
                }
            }

    }

    const T& get(const T &a)
    {
        for(int i=0;i<this->poz;i++)
            if(a==this->arr[i])
                return (const T&)this->arr[i];
        return this->err_obj;
    } 
    void set(int loc,const T &a)
    {
        if(loc<this->poz)
            return;
        this->arr[loc]=a;
    }
    int count()
    {
        return this->poz;
    }
    int firstIndexOf(const T &a, bool(*func)(T,T)=nullptr)
    {
        for(int i=0;i<this->poz;i++)
            if((func==nullptr? this->arr[i]==a : func(a,this->arr[i])))
                return i;
        return -1;
    }

};