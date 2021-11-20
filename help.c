// Datashredder help 
// Owner: awesomelewis2007
// Github:https://github.com/awesomelewis2007/Datashredder
#include<stdio.h>
#include<string.h>
int main(){
    printf("This is the Datashredder help\n");
    printf("==========\n");
    printf("Datashredder is a simple data corruption engine written in python. You can corrupt anything text, images and video.\n");
    printf("You can choose the chance of corruption e.g I have a chance of 100 therefore there is a 1 in 100 chance of the next piece of data to be corrupted this allows you to control how much corruption you want.\n");
    printf("You can also choose to have a random piece of corruption data or random e.g Corruption data is FF\n");
    printf("Not Corrupted: 30 32 35 53 f0 72\n");
    printf("Corrupted: 30 FF 35 53 FF 72\n");
    printf("A random corruption would choose a random corruption data each iteration\n");
    printf("==========\n");
    printf("Read more at:https://github.com/awesomelewis2007/Datashredder\n");
    return 0;
}