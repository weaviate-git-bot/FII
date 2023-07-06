#include <iostream>
using namespace std;


int main()
{
    int v[18]={10,432,543,5,346,5,6,7,876,1243,987,9,109,8,65,46,23};
    int size = sizeof(v)/sizeof(v[0]);
    
    auto biggestNumber = [](int *v,int size) -> int{
        cout << "Numere: " << size << '\n';
        int maxi=v[0];
        for(int i=0;i<size;i++)
            maxi = max(v[i], maxi);
        return maxi;
    };  
    cout << biggestNumber(v,size);
    
    cout <<'\n';
    return 0;
}