#include <iostream>
#include <cstring>
using namespace std;

//atoi
int a_to_i(char s[])
{
    int nr = 0;
    for(int i=0;i<strlen(s);i++)
    {
        if(s[i]>='0' && s[i]<='9')
        {
            nr = nr*10+(s[i]-'0');
        }
    }
    nr = s[0]=='-' ? -nr : nr;
    return nr;
}

int main()
{
    //read file
    FILE * file;
    file = fopen ("ini.txt","r");
    int sum = 0;
    while(!feof(file))
    {
        char line[255] = "";
        fgets(line,sizeof(line), file);
        sum += a_to_i(line);
    }
    printf("%d\n", sum);
    return 0;
}
