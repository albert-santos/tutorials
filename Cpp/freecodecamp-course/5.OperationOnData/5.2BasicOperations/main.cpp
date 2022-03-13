#include <iostream>

int main()
{   
    //Adição
    int number1{2};
    int number2{7};

    int result = number1 + number2;
    std::cout << "Result: " << result << std::endl;

    // Subtração
    result = number2 - number1;
    std::cout << "Result> " << result << std::endl;

    // Multiplicação
    result = number1 * number2;
    std::cout << "Result: " << result << std::endl;

    //Divisão
    result = number2 / number1;
    std::cout << "Result: " << result << std::endl;


    // Módulo
    result = number2 % number1; //7 % 3
    std::cout << "Result: " << result << std::endl;

    return 0;
}