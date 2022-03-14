#include <iostream>

int main()
{   
    // Declarando e inicializando ponteiros
    int* p_number {}; // é inicializado com nullptr
    double* p_fractional_number{};

    // Inicialilzando explicitamente com nullptr
    int* p_number1 {nullptr};
    double* p_fractional_number1{nullptr};

    // NOTA: ponteiros para diferentes variáveis possuem o mesmo tamanho


    // Inicializando ponteiros e atribuindo valores
    int int_var {43};
    int* p_int{&int_var};

    std::cout << "Int var: " << int_var << std::endl;
    std::cout << "p_int (Address in memory): " << p_int << std::endl;


    // Desreferenciando um ponteiro
    int* p_int2{nullptr};
    int int_data{56};
    p_int2 = &int_data;

    std::cout << "Value store in the address of the pointer: " << *p_int2 << std::endl;


    return 0;
}