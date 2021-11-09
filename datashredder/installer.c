// Datashredder Simple installer By awesomelewis2007
// Github:https://github.com/awesomelewis2007/Datashredder
#include<stdio.h>
#include<stdlib.h>
void python3_install(){
    system("python3 -m pip install --upgrade pip"); 
    system("pip install tqdm");
}
void python_install(){
    
    system("python -m pip install --upgrade pip"); 
    system("pip install tqdm");
}
int main(){
    char chr;
    printf("Welcome to the Datashredder module installer\nThe following packages will be installed: tqdm\n");
    printf("Press enter to start the install>>");
    scanf("%c",&chr);   
    python3_install();
    python_install();
}
