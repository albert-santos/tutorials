#include <iostream>

int main()
{   
    // Erro durante a compilação por causa da ausência de ; no final da linha
    // std::cout << "Hello World" << std::endl
    std::cout << "Hello World" << std::endl;


    /* 
        Erro durante a executação
        O valor não será imprimido no console por causo do erro (divisão por zero) durante a execução
    */
    int value = 7/0;
    std::cout << "value: " << value << std::endl;

    return 0;
}