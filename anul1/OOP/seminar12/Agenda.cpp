#include "Agenda.h"


Agenda::Agenda()
{

}
Contact* Agenda::searchByName(std::string name)
{
    for(auto idx: this->agenda)
    {
        if(idx->name==name)
            return idx;
    }
    return nullptr;
}

std::vector<Prieten*> Agenda::getFriendList()
{
    std::vector<Prieten*> prieteni;
    for(auto idx: this->agenda)
    {
        //????
    }
    return prieteni;
}
bool Agenda::deleteByName(std::string name)
{
    for(int i=0;i<(int)this->agenda.size();i++)
    {
        if(this->agenda[i]->name==name)
        {
            this->agenda.erase(this->agenda.begin()+i);
            return true;
        }
    }
    return false;
}
void Agenda::addContact(Contact& __contact)
{
    this->agenda.push_back(&__contact);
}