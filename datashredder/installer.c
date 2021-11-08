// Datashredder Simple installer By awesomelewis2007
// Github:https://github.com/awesomelewis2007/Datashredder
#include<stdio.h>
#include<stdlib.h>
void install(){
    system("python3 -m pip install --upgrade pip"); 
    system("pip install tqdm");
}
int main(){
    char chr;
    printf("Press enter to start the install>>");
    scanf("%c",&chr);    
    install();
}