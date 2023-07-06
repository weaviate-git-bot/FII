#pragma once
#include <iostream>
#include <cstring>


class Number
{
// add data members
private:
   char* buildStringDecimal();
   char reVal(int  n);
   int switchDecimal();
   void switchFromDecimal(int base);
   int getVal(char c);
public:
   int decimal;
   char *value;
   int base;

   Number(const char * value, int base); // where base is between 2 and 16
   Number(const int nr); // where base is between 2 and 16
   Number(const char *value);
   Number(const Number &tmp);
   Number(const Number &&tmp);
   ~Number();

   // add operators and copy/move constructor
   //index
   char operator[](int poz);
   
   //realtional
   bool operator>(const Number& B);
   bool operator>=(const Number& B);
   bool operator<(const Number& B);
   bool operator<=(const Number& B);
   bool operator==(const Number& B);
   bool operator!=(const Number& B);
   
   //negation
   void operator!();

   //asign
   void operator=(const Number& B);
   void operator=(const int nr);
   void operator=(const char* value);

   //subtract, addition
   friend Number operator+(const Number& A, const Number& B);
   friend Number operator+=(const Number& A, const Number& B);
   friend Number operator-(const Number& A, const Number& B);
   friend Number operator-=(const Number& A, const Number& B);

   //decrement
   void operator--();
   void operator--(int);


   //copy & move
   Number(Number &tmp);



   void SwitchBase(int newBase);
   void Print();
   int  GetDigitsCount(); // returns the number of digits for the current number
   int  GetBase(); // returns the current base

};