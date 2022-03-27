#include <iostream>
#include "player.h"



int main()
{   

    Player p1("Futebol");
    p1.set_first_name("Albert");
    p1.set_last_name("Santos");
    
    std::cout << "player: " << p1 << std::endl;

    
    return 0;
}