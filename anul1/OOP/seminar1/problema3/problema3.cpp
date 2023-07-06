#include <iostream>
#include <cstring>
using namespace std;
const int NMax = 255;
const char separator[] = " ";

bool comparator(const char *s1, const char *s2)
{
    if(strlen(s1)!=strlen(s2))
        return strlen(s1)<strlen(s2);
    for(int i=0;i<strlen(s1);i++)
        if(s1[i]<s2[i])
            return true;
    return false;
}
void sortare(char s[][NMax],int len)
{
    for(int i=0;i<len-1;i++)
        for(int j=i+1;j<len;j++)
            if(comparator(s[i], s[j]))
            {
                char aux[NMax];
                strcpy(aux, s[i]);
                strcpy(s[i], s[j]);
                strcpy(s[j], aux);            
            } 
}

int main()
{
    char line[NMax]="";
    char sentance[NMax][NMax];
    int siz=0;
    scanf("%[^\n]", line);
    char *p;
    p = strtok(line, separator);
    while(p!=NULL)
    {
        strcpy(sentance[siz++], p);
        p = strtok(NULL, separator);
    }
    sortare(sentance,siz);
    for(int i=0;i<siz;i++)
        printf("%s\n", sentance[i]);
    return 0;
}
