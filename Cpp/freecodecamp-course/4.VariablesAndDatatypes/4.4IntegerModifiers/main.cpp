#include <iostream>

int main()
{   
    int value1{10};
    int value2{-300};

    std::cout << "value1: " << value1 << std::endl;
    std::cout << "value2: " << value2 << std::endl;

    // Tamanho da variável em bytes
    std::cout << "sizeof(value1): " << sizeof(value1) << std::endl;
    std::cout << "sizeof(value2): " << sizeof(value2) << std::endl;

    // unsigned implica armazenar somente valores positivos
    unsigned int value3 {4};

    /*  TAMANHO DA VARIÁVEL DE ACORDO COM O MODIFICADOR

        SHORT: 2 BYTES
        INT: 4 BYTES
        LONG: 4 BYTES
        LONG LONG: 8 BYTES

    */

}