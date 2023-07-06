#pragma once
#include "Contact.h"
#include <string>

class Prieten:public Contact {
    std::string birthDate;
    std::string phoneNumber;
    std::string adress;

public:
    Prieten(std::string,std::string,std::string,std::string);
};