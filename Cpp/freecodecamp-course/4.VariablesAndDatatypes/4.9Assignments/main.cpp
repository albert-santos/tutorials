#include <iostream>

int main()
{   
    
    int var1{123}; //Declarando e inicializando
    std::cout << "var1: " << var1 << std::endl;

    var1 = 55; // Atribuição
    std::cout << "var1: " << var1 << std::endl;

    std::cout << std::endl;

    std::cout<< "----------------" << std::endl;


    double var2 {44.55}; //Declarando e inicializando
    std::cout << "var2: " << var2 << std::endl;

    var2 = 99.99; // Atribuição
    std::cout << "var2: " << var2 << std::endl;

    std::cout<< "----------------" << std::endl;


    bool state{false}; //Declarando e inicializando
    std::cout << std::boolalpha;
    std::cout << "state: " << state << std::endl;

    state = true; //Atribuindo

    std::cout << "state: " << state << std::endl;



    return 0;
}