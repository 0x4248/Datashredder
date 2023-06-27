// Datashredder help 
// Owner: lewisevans2007
// Github:https://github.com/lewisevans2007/Datashredder
#include <iostream>
#include <string>
#include <limits>
using namespace std;
int main(){
    cout << "\033[0;36mThis is the Datashredder help\n";
    cout << "\033[0;36m==========\n";
    cout << "\033[0;37mDatashredder is a simple data corruption engine written in python. You can corrupt anything text, images and video.\n";
    cout << "You can choose the chance of corruption e.g I have a chance of 100 therefore there is a 1 in 100 chance of the next piece of data to be corrupted this allows you to control how much corruption you want.\n";
    cout << "You can also choose to have a random piece of corruption data or random e.g Corruption data is FF\n";
    cout << "Not Corrupted: 30 32 35 53 f0 72\n";
    cout << "Corrupted: 30 FF 35 53 FF 72\n";
    cout << "A random corruption would choose a random corruption data each iteration\n";
    cout << "\033[0;36m==========\n";
    cout << "\033[0;32mPress Enter to read more>";
    cin.ignore(std::numeric_limits<streamsize>::max(),'\n');
    cout << "\033[0;37mInstalling\n";
    cout << "You can install datashredder using pip \npip install Datashredder\n";
    cout << "\033[0;36m==========\n";
    cout << "\033[0;37mThe next section contains images\n";
    cout << "Read more at:https://github.com/lewisevans2007/Datashredder\n";
    return 0;
}