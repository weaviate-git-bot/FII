#pragma once
#include "Contact.h"
#include <string>

class Coleg:public Contact {
    std::string phoneNumber;
    std::string workPlace;
    std::string adress;
public:
    Coleg(std::string,std::string,std::string,std::string);

};