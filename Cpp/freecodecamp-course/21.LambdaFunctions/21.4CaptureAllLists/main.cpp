#include <iostream>

int main() {

/*  
    //capturar tudo por valor
    int c{42};

    auto func = [=](){
        std::cout << "Dentro da função: " << c << std::endl;
    };

    for (size_t i{}; i < 5 ; ++i){
        std::cout << "Valor fora da função: " << c << std::endl;
        func();
        ++c;
    }
*/

    //Capturando tudo por referência
    int c{42};
    int d{5}
;
    auto func = [&](){
        std::cout << "Dentro da função: " << c << std::endl;
        std::cout << "Dentro da função: " << d << std::endl;
    };

    for (size_t i{}; i < 5 ; ++i){
        std::cout << "Valor fora da função: " << c << std::endl;
        func();
        ++c;
    }

    return 0;
}