#pragma once
#include "Contact.h"
#include "Prieten.h"
#include <vector>
#include <string>
#include <iostream>

class Agenda {
    std::vector<Contact*> agenda;

public:
    Agenda();
    Contact* searchByName(std::string);
    std::vector<Prieten*> getFriendList();
    bool deleteByName(std::string);
    void addContact(Contact&);
};