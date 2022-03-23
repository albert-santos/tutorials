#include <iostream>

int main() {
    
    //capture lists

/*
    double a{10};
    double b {20};

    auto func= [a, b]() {
        std::cout << "a + b: " << a + b << std::endl;
    };

    func();
*/

/*
    // Capturando pelo valor
    // Cria uma cópia do está sendo captura
    int c{42};
    auto func = [c](){
        std::cout << "Valor dentro da função lambda: " << c << ". &dentro: " << &c << std::endl;
    };

    for (size_t i{}; i<5; ++i){
        std::cout << "Valor fora da função lambda: " << c << ". &fora: " << &c << std::endl;
        func();
        ++c; // incrementa o valor de c que está fora da função lambda
    }
*/



    //Capturando por referência
    // Não cria uma cópia. Qualquer alteração dentro da função lambda afeta diretamente a variável capturada
    int c{42};
    auto func = [&c](){
        std::cout << "Valor dentro da função lambda: " << c << ". &dentro: " << &c << std::endl;
    };

    for (size_t i{}; i<5; ++i){
        std::cout << "Valor fora da função lambda: " << c << ". &fora: " << &c << std::endl;
        func();
        ++c; // incrementa o valor de c que está fora da função lambda
    }

    return 0;
}