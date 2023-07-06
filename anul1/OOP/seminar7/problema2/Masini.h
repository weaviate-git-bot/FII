class Masini 
{
    int rezervor;
    int putere;

public:
    Masini();
    Masini(int,int);
    int getPutere() const;
    int getRezervor() const;
    friend bool operator<(const Masini&,const Masini&);
    friend bool operator==(const Masini&,const Masini&);
};