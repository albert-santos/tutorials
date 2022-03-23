#include <iostream>

template <typename T> const T& maximum(const T& a, const T& b); // Declaração do template 

int main() {
    
    double a{23.5};
    double b{51.2};

    auto result = maximum(a, b);
    std::cout << "Out - &a: " << &a << std::endl;

    return 0;
}

//Definição do template da função
template <typename T> const T& maximum(const T& a, const T& b) {
    std::cout << "In - &a: " << &a << std::endl;
    return (a > b) ? a : b; 
}