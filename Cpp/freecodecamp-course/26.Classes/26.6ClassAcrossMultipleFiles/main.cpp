#include <iostream>
#include "cylinder.h"


int main()
{   
    Cylinder cylinder1(10,40);
    std::cout << "volume: " << cylinder1.volume() << std::endl;

    return 0;
}