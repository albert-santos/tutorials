#include <iostream>

template <typename T> const T& maximum(const T& a, const T& b); // Declaração do template 

int main() {
    
    double a{23.5};
    double b{51.2};

    auto result = maximum(a, b);
    std::cout << "Out - &a: " << &a << std::endl;


    std::string x1 {"animation_SDN"};
    std::string x2 {".xml"};

    int i {0};

    std::string aux = std::to_string(i);

    std::string concat = x1 + aux + x2; 

    std::cout << concat << std::endl;

    return 0;
}

//Definição do template da função
template <typename T> const T& maximum(const T& a, const T& b) {
    std::cout << "In - &a: " << &a << std::endl;
    return (a > b) ? a : b; 
}