#include "Math.h"
using namespace std;

int Math::Add(int a,int b)
{
    return (a+b);
}
int Math::Add(int a,int b,int c)
{
    return (a+b+c);
}

double Math::Add(double a,double b)
{
    return (a+b)*1.0;
}
double Math::Add(double a,double b,double c)
{
    return (a+b+c);
}
double Math::Add(int a,double b)
{
    return ((a*1.0)+b);
}
int Math::Mul(int a,int b)
{
    return (a*b);
}

int Math::Mul(int a,int b,int c)
{
    return (a*b*c);
}

double Math::Mul(double a,double b)
{
    return (a*b);
}
double Math::Mul(double a,double b,double c)
{
    return (int)(a*b*c);
}

int Math::Add(int count, ...)
{
    va_list args;
    va_start(args, count);
    int sum=0;
    for(int i=0;i<count;i++)
    {
        int x = va_arg(args,int);
        sum  += x;
    }
    va_end(args);
    return sum;
}

char* Math::Add(const char *a, const char *b)
{
    if(a==nullptr || b==nullptr)
        return nullptr;
    int len1 = strlen(a);
    int len2 = strlen(b);
    char *str = new char[len1+len2+10];
    for(int i=0;i<len1;i++)
        str[i]=a[i];

    for(int i=len1;i<len1+len2;i++)
    {
        str[i]=b[i-len1];
    }

    str[len1+len2] = '\0';
    return str;
}