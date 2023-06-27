// Datashredder Simple installer
// Owner: lewisevans2007
// Github:https://github.com/lewisevans2007/Datashredder
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
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
    char str1[8];
    printf("Do you use python3 or python:");
    scanf("%s", str1);
    if(strcmp(str1, "python3")==0){
        python3_install();
        return 0;
    }else if(strcmp(str1, "python")==0){
        python_install();
        return 0;
    } else {
        python_install();
        python3_install(); 
        return 0;
    }
    return 0;
}
