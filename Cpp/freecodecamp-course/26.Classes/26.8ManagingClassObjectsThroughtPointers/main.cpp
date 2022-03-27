#include <iostream>
#include "cylinder.h"


int main()
{   
    Cylinder cylinder1(10,40);

    std::cout << "volume: " << cylinder1.volume() << std::endl;

    // Gerenciando um objeto stack através de ponteiros
    Cylinder* p_cylinder1 = &cylinder1;
    //std::cout << "volume: " << (*p_cylinder1).volume() << std::endl;
    std::cout << "volume: " << p_cylinder1->volume() << std::endl;

    // Criando um objeto heap através do operador new
    Cylinder* p_cylinder2 = new Cylinder(100,2);
    std::cout<<"volume(cylinder2): " << p_cylinder2->volume() << std::endl;
    std::cout << "base_radius(cylinder2): " << p_cylinder2->get_base_radius() << std::endl;




    delete p_cylinder2;

    return 0;
}