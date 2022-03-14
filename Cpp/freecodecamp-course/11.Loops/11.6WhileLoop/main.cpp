#include <iostream>

int main()
{   
    
    const size_t COUNT{10}; // Quantas vezes o loop será repetido
    size_t i {0}; // Declaração do iterator

    while(i < COUNT){ // Condição de parada do loop
    
        std::cout << i << ": I love C++" << std::endl;

        ++i; //incremento do iterator
    }


    std::cout << "Loop done!" << std::endl;

    return 0;
}