#pragma once
#include "Contact.h"
#include <string>

class Cunoscut:public Contact {
    std::string phoneNumber;
public: 
    Cunoscut(std::string,std::string);
};