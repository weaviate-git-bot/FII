#include "Number.h"
using namespace std;

Number::Number(const char *value, int base)
{
    if(base<2 || base>16)
    {
        cout <<"Couldn't initialize class\n";
        return;
    }
    this->value = new char[strlen(value)+3];
    strcpy(this->value,  value);
    this->base=base;
    this->decimal = this->switchDecimal();
}
   
Number::Number(const int nr)
{
    this->base=10;
    this->decimal=nr;
    this->value = new char[16];
    this->value = this->buildStringDecimal();
}
Number::Number(const char *value)
{
    this->value = new char[strlen(value)+3];
    strcpy(this->value,  value);
    this->base=10;
    this->decimal = this->switchDecimal();
}
Number::~Number()
{
    delete this->value;
    this->base=0;
}

void Number::SwitchBase(int newBase)
{
    if(newBase==10)
        this->value=this->buildStringDecimal();
    else
    {
        this->switchFromDecimal(newBase);
        this->decimal = this->switchDecimal();    
    } 
}
void Number::Print()
{
    cout << this->value<<'\n';
}
int  Number::GetDigitsCount()
{
    return strlen(this->value);
}
int  Number::GetBase()
{
    return this->base;
}

int Number::getVal(char c)
{
    if(c>='0' && c<='9')
        return (int)c-'0';

    return (int)c-'A'+10;
}

int Number::switchDecimal()
{
    int len = strlen(this->value);
    int power = 1;
    int num = 0;

    for(int i=len-1;i>=0;i--)
    {
        num += this->getVal(this->value[i])*power;
        power*=base;
    }
    return num;

}
char Number::reVal(int  n)
{
    if(n>=0 && n<=9)
        return n+'0';
    return n-10+'A';
}
void Number::switchFromDecimal(int base)
{
    int poz=0;
    int cn = this->decimal;
    char *newbase = new char[strlen(this->value)*2];

    while(cn>0)
    {
        newbase[poz++]=reVal(cn%base);
        cn/=base;
    }
    newbase[poz]='\0';
    this->base = base;
    int baselen = strlen(newbase);
    for(int i=0;i<baselen/2;i++)
        swap(newbase[i], newbase[baselen-i-1]);
    delete this->value;
    this->value = new char[baselen+10];
    this->value = newbase;
}
char* Number::buildStringDecimal()
{
    int len = strlen(this->value);
    char* base = new char[len+5];
    int poz = 0;
    int cn  = this->decimal;
    while(cn)
    {
        base[poz++] = cn%10+'0';
        cn/=10;
    }
    for(int i=0;i<poz/2;i++)
        swap(base[i],  base[poz-i-1]);
    base[poz]='\0';
    return base;
}
void Number::operator=(const Number& B)
{
    this->decimal = B.decimal;
    this->value = this->buildStringDecimal();
    this->SwitchBase(this->base);
}
void Number::operator=(const char* value)
{
    delete this->value;
    this->value = new char[strlen(value)+5];
    strcpy(this->value, value);

    int abase=this->base;
    this->base = 10;
    this->SwitchBase(abase);
}
void Number::operator=(const int nr)
{
    this->decimal=nr;
    int abase=this->base;
    this->base = 10;
    this->SwitchBase(abase);
}
char Number::operator[](int poz)
{
    return this->value[poz];
}
bool Number::operator>(const Number& B)
{
    return (this->decimal>B.decimal);
}
bool Number::operator>=(const Number& B)
{
    return (this->decimal>=B.decimal);
}
bool Number::operator<(const Number& B)
{
    return (this->decimal<B.decimal);
}
bool Number::operator<=(const Number& B)
{
    return (this->decimal<=B.decimal);
}
bool Number::operator==(const Number& B)
{
    return (this->decimal==B.decimal);
}
bool Number::operator!=(const Number& B)
{
    return (this->decimal!=B.decimal);
}

void Number::operator!()
{
    
    int abase = this->base;
    this->SwitchBase(2);
    for(int i=0;i<strlen(this->value);i++)
        this->value[i]=(this->value[i]=='0' ? '1' : '0');
    this->SwitchBase(abase);
}

Number::Number(const Number &tmp)
{
    this->value = tmp.value;
    this->base = tmp.base;
    this->decimal = tmp.decimal;
}

Number::Number(const Number &&tmp)
{
    delete this->value;
    int len = strlen(tmp.value);
    this->value = new char[len+3];
    strcpy(this->value, tmp.value);
    this->base = tmp.base;
    this->decimal = tmp.decimal;
}
Number operator+(const Number& A, const Number& B)
{
    int val = A.decimal + B.decimal;
    int base = max(A.base, B.base);
    Number tmp = val;
    tmp.SwitchBase(base);
    return tmp; 
}
Number operator+=(const Number& A, const Number& B)
{
    int val = A.decimal + B.decimal;
    int base = max(A.base, B.base);
    Number tmp = val;
    tmp.SwitchBase(base);
    return tmp;
}
Number operator-(const Number& A, const Number& B)
{
    int val = A.decimal - B.decimal;
    int base = max(A.base, B.base);
    Number tmp = val;
    tmp.SwitchBase(base);
    return tmp;
}
Number operator-=(const Number& A, const Number& B)
{
    int val = A.decimal - B.decimal;
    int base = max(A.base, B.base);
    Number tmp = val;
    tmp.SwitchBase(base);
    return tmp;
}
// void Number::operator=(const Number& B)
// {
//     this = *B;
// }
void Number::operator--()
{
    int len = strlen(this->value);
    for(int i=0;i<len;i++)
        this->value[i] = this->value[i+1];
    this->value[len-1]='\0';
    this->decimal = this->switchDecimal();
}
void Number::operator--(int)
{
    int len = strlen(this->value);
    this->value[len-1]='\0';
}

/**
 * & copiere
 * && mutare
 * */