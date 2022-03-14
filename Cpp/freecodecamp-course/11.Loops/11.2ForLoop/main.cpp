#include <iostream>

int main()
{   
    //For loop

/*
    for(unsigned int i{}; i < 10 ; ++i){
        std::cout << i << ": I love C++ " << std::endl;
    }

    
*/

    // Utilizando size_t para representar números positivos [por exemplo, tamanho de algo]
/*
    for (size_t i{}; i < 10 ; ++i){
        std::cout << i << ": I love C++" << std::endl;
    }

*/

/*
    //Declarando o iterator fora do loop
    size_t i {0};
    
    for(i; i < 10 ; ++i){
        std::cout << i << ": I love C++" << std::endl;
    }

*/


    // Valor de parada inicializado fora do loop

    const size_t COUNT{10};

    for(size_t i{0}; i < COUNT ; ++i){
        std::cout << i << ": I love C++" << std::endl;

    }




    std::cout << "Loop done!" << std::endl;

    return 0;

}