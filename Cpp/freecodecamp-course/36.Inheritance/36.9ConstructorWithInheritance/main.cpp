#include <iostream>
#include "person.h"
#include "engineer.h"
#include "civilengineer.h"

int main(){

    Person person1("Albert Santos", 23, "Belém");
    std::cout << "person 1: " << person1 << std::endl;

    Engineer eng1("Mr", 28, "Address 2", 12);
    std::cout << "eng1: " << eng1 << std::endl;
    CivilEngineer ce1("Nome 3", 26, "Add 3", 11, "Especialidade 3");
    std::cout << "person 3: " << ce1 << std::endl;
   
    return 0;
}