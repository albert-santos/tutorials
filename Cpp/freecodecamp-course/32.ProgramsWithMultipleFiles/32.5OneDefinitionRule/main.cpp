#include <iostream>

//Definição e declaração da variável
double weight {};

//declaração da função
double add(double a, double b);

int main()
{   
    //std::cout << weight << std::endl;

    double result = add(10, 20);
    std::cout << result << std::endl;

    return 0;
}

// Definição da função
double add(double a , double b) {
    return a + b;
}